from bs4 import*
from unidecode import unidecode
import json

def plaintext(url):
  soup = BeautifulSoup(url)
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
  ligne = p.split("\n")
  team = []
  for l in ligne:
    l = l.replace("(M)","").replace("(F)","").replace(" ","")
    if "(" and ")" in l:
      #print("y " + l)
      l = l[ l.find( '(' )+1 : l.find( ')' ) ]
      team.append(l)
    elif "@" in l:
      #print("n " + l)
      l = l.split("@")[0]
      team.append(l)
  return team