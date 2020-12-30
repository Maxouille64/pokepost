#samantha and ariana
from flask import Flask, render_template, request, render_template_string, send_file, Response, redirect, url_for
from parse import plaintext, get_title, get_author, get_notes, get_paste, get_pokes
from packing import export_to_packed
import logging
import csv 
import urllib
import datetime
import requests

app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route("/")
def test():
  return render_template("index.html", title="Pokepost!")

@app.route("/data")
def data():
  return send_file('data.csv')

@app.route("/a")
def a():
  return render_template("a.html")

@app.route("/dn")
def dn():
  return redirect("https://www.youtube.com/watch?v=2mUeKNqy490", code=302)

@app.route("/index1")
def hello():
  cookie = request.cookies.get('username')
  if cookie == None:
    cookie = "Random strat"
  else:
    pass
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
          "Title": row[5],
          "Author": row[4],
          "Notes": row[6],
          "Paste": row[9]
        })
      #After the first iteration first_line is set to false  
      else:
        first_line = False
  #art = art_data for simplicity in html  
  return render_template("index1.html", art = art_data, title = "Upload team", username = cookie)

@app.route("/raw/", methods=['POST'])
def raw():
    #Moving forward code
    print(request.args.get('paste'))
    return request.args.get('paste')


@app.route('/result', methods=["POST", "GET"])
def result():
  if request.method == 'POST':
    #Gather data from form
    date = datetime.datetime.now()
    userdata = dict(request.form)
    tags = ''
    
    url = userdata["team"][0]
    pseudo = userdata["pseudo"][0].replace(",","/")
    if ("pokepast.es" in url):
      pass
    elif ("pastebin.com" in url):
      return "only work with pokepast.es for now :("
    else:
      erreur = (str(date) + " -> " + url + "|" + pseudo)
      cahier = open("log.txt" ,"a")
      cahier.write("\n" + erreur)
      cahier.close
      print("AAAAAAAAAAAAH!!!" + erreur)
      return "ENVOIE UN PASTE GOGOL!!! ex: https://pokepast.es/1 (si c une erreur elle a ete sauvegarde n'hesite pas a m'avertir)"
    gen = userdata["gen"][0].split("|")
    tier = userdata["tier"][0]
    format = gen[0] + tier
    
    json = urllib.urlopen(url + "/json").read()
    raw = urllib.urlopen(url + "/raw").read()
    
    rawjson = plaintext(json)
    
    rawpaste = plaintext(raw)
    #print("POKEPASTE: " + rawpaste)
    
    title = get_title(rawjson).replace(",","/")
    author = get_author(rawjson).replace(",","/")
    notes = get_notes(rawjson).replace(",","/")
    paste = export_to_packed(get_paste(rawjson))
    print(paste)
    pokes = get_pokes(rawpaste)
    print("author" + author)
    
    team = ''
    for poke in pokes:
      team = team + poke + "|"
    n = 6 - team.count("|")
    while n>0:
      n = n - 1
      team = team + "0|"
      
    tags = "||" + gen[0] + "|" + gen[1] + "|" + tier + "|" + author + "|" + pseudo + "|"

    #open file and write data to it
    with open('data.csv', mode='a') as csv_file:
      data = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data.writerow([url, format, date, pseudo, author, title, notes, team, tags, paste])
    return render_template("result.html", title ="Success")
  else:
    return render_template("index2.html", title="CSV")
  


    
if __name__ == "__main__":
  app.run()
