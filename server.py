#samantha and ariana
from flask import Flask, render_template, request, render_template_string, send_file, Response, redirect, url_for, jsonify
from parse import plaintext, get_title, get_author, get_notes, get_paste, get_pokes
from team_converter import export_to_packed, packed_to_json
import logging
import csv 
import urllib
import datetime
import requests

app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route("/")
def index():
  return render_template("index.html", title="Pokepost v2")
  #return render_template("maintenance.html", title="Pokepost.tk/")

@app.route("/data")
def data():
  return send_file('data.csv')

@app.route("/a")
def a():
  return render_template("a.html")

@app.route("/upload")
def hello():
  cookie = request.cookies.get('username')
  if cookie == None:
    cookie = "guest"
    art_data = [{'Notes': 'dont pay attention to this','Paste': 'hey! ouste'}]
  elif cookie == "Maxouille":
      #open and read data 
      with open('data.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        #set a first line variable so loop doesn't run the first time
        first_line = True
        #art_data list to house data
        art_data = []
        for row in data:
          #assigning data to the list to later be printed on the html
          if not first_line and row[8] == ("[u'on']"):
            art_data.append({
              "Title": row[5],
              "Author": row[3],
              "Notes": row[6],
              "Paste": row[10]
            })
            #print(art_data)
          #After the first iteration first_line is set to false  
          else:
            first_line = False
  else:
    art_data = []
    pass

  #art = art_data for simplicity in html  
  return render_template("upload.html", art = art_data, title = "Upload team", username = cookie)

@app.route("/raw/", methods=['POST'])
def raw():
    #Moving forward code
    pack = str(request.args.get('paste'))
    print(pack)
    team_json = packed_to_json(pack)
    return jsonify(team_json)
  
@app.route("/dn/", methods=['POST'])
def dn():
  date = datetime.datetime.now()
  err = request.args.get('err')
  log = open("log.txt" ,"a")
  log.write("\n" + str(date) + " -> " + err)
  log.close
  return "erreur fatale"


@app.route('/result', methods=["POST", "GET"])
def result():
  if request.method == 'POST':
    #Gather data from form
    date = datetime.datetime.now()
    userdata = dict(request.form)
    tags = ''
    isprivate = "[u'off']"
    
    url = userdata["team"][0]
    pseudo = request.cookies.get('username')
    if pseudo == None:
      pseudo = "Random strat"
    else:
      isprivate = request.form.getlist('private')
      pseudo = pseudo.replace(",","/")
      
    if ("pokepast.es/" in url):
      pass
    elif ("pastebin.com" in url):
      return "only work with pokepast.es for now :("
    else:
      erreur = (str(date) + " -> " + url + "|" + pseudo)
      cahier = open("log.txt" ,"a")
      cahier.write("\n" + erreur)
      cahier.close
      title = pseudo + "'s super cool team"
      myobj = [('paste',url),('author',pseudo),('title',title)]
      url = requests.post("https://pokepast.es/create", data = myobj)
      url = url.url
      #return "only pokepast format is supported ex: https://pokepast.es/1 (errors are reported anyway)"
    gen = userdata["gen"][0].split("|")
    tier = userdata["tier"][0]
    format = gen[0] + tier
    
    json = urllib.urlopen(url + "/json").read()
    raw = urllib.urlopen(url + "/raw").read()
    #plus besoin du prefixe de l'url
    url = url.split("pokepast.es/")[1]
    
    rawjson = plaintext(json)
    
    rawpaste = plaintext(raw)
    #print("POKEPASTE: " + rawpaste)
    
    print("GET PASTE...")
    author = get_author(rawjson).replace(",","/comma/")
    title = get_title(rawjson).replace(",","/comma/") + " by " + author
    notes = get_notes(rawjson).replace(",","/comma/")
    team_json = get_paste(rawjson)
    print("|" + team_json.strip() + "|")
    pack = export_to_packed(team_json.strip())
    print("PACKING...")
    print(pack)
    pokes = get_pokes(rawpaste)
    print("author " + author)
    
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
      data.writerow([url, format, date, pseudo, title, notes, team, isprivate, tags, pack])
    return render_template("result.html", title ="Success")
  else:
    return render_template("index2.html", title="CSV")
  


    
if __name__ == "__main__":
  app.run()
