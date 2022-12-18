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

method_requests_mapping = {
    'GET': requests.get,
    'HEAD': requests.head,
    'POST': requests.post,
    'PUT': requests.put,
    'DELETE': requests.delete,
    'PATCH': requests.patch,
    'OPTIONS': requests.options,
}

@app.route("/")
def index():
  return render_template("index.html", title="Pokepost v3")
  #return render_template("maintenance.html", title="Pokepost.tk/")
  
@app.route("/data")
def data():
  return send_file('data.csv')
  
@app.route("/download")
def firefox():
  return redirect("https://cdn.glitch.me/c7b08ba3-0914-48ee-91c4-a9884f3b0ce9/RTB.xpi?v=1639684912571", code=302)

@app.route("/a")
def a():
  return render_template("a.html")

@app.route("/upload")
def upload():
  cookie = request.cookies.get('username')
  if cookie == None:
    cookie = "guest"
  return render_template("upload.html", title = "Upload team", username = cookie)

@app.route("/raw/", methods=['POST'])
def json():
    #Moving forward code
    print(request.args, flush=True)
    pack = str(request.args.get('paste'))
    team_json = packed_to_json(pack)
    return jsonify(team_json)
  
@app.route('/post', methods=["POST"])
def json2():
    print(request.form, flush=True)
    #Moving forward code
    requests_function = method_requests_mapping[request.method]
    rep = requests.post("https://play.pokemonshowdown.com/~~showdown/action.php", data = request.form)
    return rep.text
  
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
    
    url = userdata["paste"]
    pseudo = request.cookies.get('username')
    if pseudo == None:
      pseudo = "Random strat"
    else:
      isprivate = request.form.getlist('private')
      pseudo = pseudo.replace(",","/")
      
    if ("pokepast.es/" in url):
      json = urllib.request.urlopen(url + "/json").read()
      rawpaste = urllib.request.urlopen(url + "/raw").read()
      rawpaste = plaintext(rawpaste)
      #print(rawpaste, flush=True)
      rawjson = plaintext(json)
      author = get_author(rawjson).replace(",","/comma/")
      title = get_title(rawjson).replace(",","/comma/") + " by " + author
      notes = get_notes(rawjson).replace(",","/comma/")
      print("author " + author, flush=True)
      pass
    elif ("pastebin.com" in url):
      return "only work with pokepast.es for now :("
    else:
      print("ELSE", flush=True)
      rawpaste = str(url.strip())
      notes = "[u'raw']"
      title = pseudo + "'s super cool team"
      myobj = [('paste',url),('author',pseudo),('title',title)]
      url = requests.post("https://pokepast.es/create", data = myobj)
      url = url.url
      if url == "https://pokepast.es/create":
        return "No (or Invalid) Paste"    
    if userdata["title"] != "":
      title = userdata["title"]
      print("title", flush=True)
      print(title, flush=True)
      
    url = url.split("pokepast.es/")[1]      
    title = plaintext(title)
    gen = (userdata["gen"].replace("u","")).split("|")
    print("GEN", flush=True)
    tier = userdata["tier"]
    format = gen[0] + tier
    
    pack = export_to_packed(rawpaste)
    print("PACK", flush=True)
    print(pack, flush=True)
    pokes = get_pokes(rawpaste)
    
    team = ''
    for poke in pokes:
      print(">",poke, flush=True)
      team = team + poke + "|"
    n = 6 - team.count("|")
    while n>0:
      n = n - 1
      team = team + "0|"
      
    tags = "||" + gen[0] + "|" + gen[0] + "|" + tier + "|" + title + "|" + pseudo + "|"

    #open file and write data to it
    with open('data.csv', mode='a') as csv_file:
      data = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      data.writerow([url, format, date, pseudo, title, notes, team, isprivate, tags, pack])
    return render_template("result.html", title ="Success")
  else:
    cookie = request.cookies.get('username')
    if cookie == "Maxouille":
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
                "Url": row[0],
                "Format": row[1],
                "Date": row[2],
                "Author": row[3],
                "Title": row[4],
                "Notes": row[5],
                "Team": row[6],
                "isPrivate": row[7],
                "Tags": row[8],
                "Paste": row[9]
              })
              #print(art_data, flush=True)
            #After the first iteration first_line is set to false  
            else:
              first_line = False
    else:
      art_data = []
      pass

    #art = art_data for simplicity in html  
    return render_template("index2.html", art = art_data, title = "CSV")
    
if __name__ == "__main__":
  app.run()
