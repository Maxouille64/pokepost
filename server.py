#samantha and ariana
from flask import Flask, render_template,request,render_template_string, send_file
from parse import plaintext, get_title, get_author, get_notes, get_paste
import logging
import csv 
import urllib
app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route("/")
def test():
  return render_template("index.html")

@app.route("/data")
def data():
  return send_file('data.csv')

@app.route("/art")
def art():
  return send_file('art.csv')
  
@app.route("/index1")
def hello():
  #open and read data
  with open('data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    #set a first line variable so loop doesn't run the first time
    first_line = True
    #art_data list to house data
    art_data = []
    for row in data:
      #assigning data to the list to later be printed on the html
      if not first_line:
        art_data.append({
          "Title": row[0],
          "Author": row[1],
          "Notes": row[2],
          "Paste": row[3]
        })
      #After the first iteration first_line is set to false  
      else:
        first_line = False
  #art = art_data for simplicity in html      
  return render_template("index1.html", art = art_data, title = "Upload team")
  


@app.route('/result', methods=["POST", "GET"])
def result():
  if request.method == 'POST':
    #Gather data from form
    userdata = dict(request.form)
    team = userdata["team"][0]
    json = urllib.urlopen(team + "/json").read()
    raw = urllib.urlopen(team + "/raw").read()
    
    rawjson = plaintext(json)
    
    rawpaste = plaintext(raw)
    #print("POKEPASTE: " + rawpaste)
    
    title = get_title(rawjson)
    author = get_author(rawjson)
    notes = get_notes(rawjson)
    pokes = get_paste(rawpaste)
    print("author" + author)
    team = ''
    for poke in pokes:
      team = team + poke + "|"

    #open file and write data to it
    with open('data.csv', mode='a') as csv_file:
      data = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data.writerow([title, author, notes, team])
    return render_template("index.html", title ="Success")
  else:
    return render_template("result.html", title="CSV")
  


    
if __name__ == "__main__":
  app.run()
