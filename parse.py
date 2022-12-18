from bs4 import*
from unidecode import unidecode
import json

def plaintext(url):
  soup = BeautifulSoup(url, features="html.parser")
  text = soup.get_text()
  unicodetext = unidecode(text)
  return unicodetext

def get_title(x):
  data = json.loads(x)
  title = data["title"]
  if title == "":
    return "Sans titre"
  else:
    return title
    
def get_author(y):
  data = json.loads(y)
  author = data["author"]
  if author == "":
    return "???"
  else:
    return author

def get_notes(z):
  data = json.loads(z)
  return data["notes"]

def get_paste(t):
  data = json.loads(t)
  return data["paste"]

def get_pokes(p):
  sets = p.split("\r\n\r\n")
  team = []
  for set in sets:
    l = set.split("\r\n")[0].replace("(M)","").replace("(F)","").replace(" ","")
    if "(" and ")" in l:
      #print("y " + l)
      l = l[ l.find( '(' )+1 : l.find( ')' ) ]
      team.append(l)
    elif "@" in l:
      #print("n " + l)
      l = l.split("@")[0]
      team.append(l)
    else:
      team.append(l)
  return team