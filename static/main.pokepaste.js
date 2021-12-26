//THIS CODE SHOWS PASTES USING `https://pokepast.es/`
const tagContainer = document.querySelector('.tag-container');
const input = document.querySelector('.tag-container input');
let tags = [];
var tag = null

document.getElementById("demo").innerHTML = "#" ;

//TAG Search
function createTag(label) {
  const div = document.createElement('div');
  div.setAttribute('class', 'tag');
  const span = document.createElement('span');
  span.innerHTML = label;
  const closeIcon = document.createElement('i');
  closeIcon.innerHTML = 'close';
  closeIcon.setAttribute('class', 'material-icons');
  closeIcon.setAttribute('data-item', label);
  div.appendChild(span);
  div.appendChild(closeIcon);
  return div;
}

function clearTags() {
  document.querySelectorAll('.tag').forEach(tag => {
    tag.parentElement.removeChild(tag);
  });
}

function addTags() {
  clearTags();
  tags.slice().reverse().forEach(tag => {
    tagContainer.prepend(createTag(tag));
  });
}

function myFunction(item) {
    var filter, ul, li, i, txtValue;
    //filter = "|" + item.toUpperCase() + "|";
    filter = item.toUpperCase();
    ul = document.getElementById("myMenu");
    li = ul.getElementsByTagName("li");
    document.getElementById("demo").innerHTML = "#" + tags;
    for (i = 0; i < li.length; i++) {
        //a = li[i].getElementsByTagName("a")[0];
        //txtValue = a.textContent || a.innerText;
        txtValue = li[i].getAttribute("tags");
        //console.log(txtValue)
        if (tag != null) {
          li[i].style.display = ""; 
        }
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            void(0)
        } else {
            li[i].style.display = "none";
        }
    }
    tag = null
}

input.addEventListener('keyup', (e) => {
    if (e.key === 'Enter') {
      e.target.value.split(',').forEach(tag => {
        tags.push(tag);
        tags.forEach(myFunction);
      });
      
      addTags();
      input.value = '';
    }
});
document.addEventListener('click', (e) => {
  console.log(tags);
  if (e.target.tagName === 'I') {
    const tagLabel = e.target.getAttribute('data-item');
    const index = tags.indexOf(tagLabel);
    tags = [...tags.slice(0, index), ...tags.slice(index+1)];
    addTags();
    tag = tagLabel;
    tags.forEach(myFunction);
  }
  if (tags.length == 0) {
      let tags = [""];
      tags.forEach(myFunction);
  }
  console.log(tags.length)
})

input.focus();

//Display teams
function getCookie(cname) {
var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

async function Display() {
  try {
    const response = await fetch('data')
    const CSV = await response.text();
    //const response1 = await fetch("dexdata.json");
    //const json = await response1.json();
    const arrCSV = CSV.split('\n').reverse();
    const ul = document.getElementById("myMenu")
    for (var i = 1, len = arrCSV.length; i < len; i++) {
      var indice = arrCSV[i].split(",");
      var isprivate = indice[7];
      var username = indice[3];
      var cookie = getCookie("username");
      if (isprivate.indexOf("on") === -1 ||cookie.toUpperCase() == username.toUpperCase()) {
        var li = document.createElement("li");
        var x0 = document.createElement("TABLE");
        var y0 = document.createElement("TR");
        var y1 = document.createElement("TR"); 
        var z0 = document.createElement("TD");
        var z1 = document.createElement("TD");
        var a = document.createElement("A");
        var b = document.createElement("B");
        var s0 = document.createElement("IMG");
        var s1 = document.createElement("IMG");
        var s2 = document.createElement("IMG");
        var s3 = document.createElement("IMG");
        var s4 = document.createElement("IMG");
        var s5 = document.createElement("IMG");
        var auth = document.createElement("DIV");
        var url = "https://play.pokemonshowdown.com/sprites/gen5/"
        var team = indice[6]
        var team = team.replace("Urshifu-Rapid-Strike","urshifu-rapidstrike");
        var team = team.replace("Mega-X","megax");
        var team = team.replace("Mega-Y","megay");
        var team = team.replace("Ho-Oh","hooh");
        var team = team.replace("Kommo-o","kommoo");
        var team = team.replace("%","");
        var tags = indice[8] + team;
        var poke = team.split("|");
        var title = "[" + indice[1].toUpperCase() + "] " + indice[4];
        var text = document.createTextNode("");
        var date = document.createTextNode("Added the " + indice[2] + " by " + username);
        var saut = document.createElement("BR");
        li.setAttribute("tags", tags);
        ul.appendChild(li);
        li.appendChild(saut);
        li.appendChild(x0);
        y0.setAttribute("id", "myTr" + [i]);
        y1.setAttribute("id", "yourTr" + [i]);
        x0.appendChild(y0);
        x0.appendChild(y1);
        z0.style.background = "rgba(102 , 136 , 170 , 0.40)";
        a.setAttribute("id", "a" + [i])
        a.setAttribute("href", "https://pokepast.es/" + indice[0]);
        a.setAttribute("target", "_blank");
        a.setAttribute("rel", "noopener");
        //go mettre des <img> plutot!
        Object.assign(s0, {
          style: 'margin-left: 2px',
          src: url + poke[0].toLowerCase() + ".png"
        });
        Object.assign(s1, {
          style: 'margin-left: 2px',
          src: url + poke[1].toLowerCase() + ".png"
        });
        Object.assign(s2, {
          style: 'margin-left: 2px',
          src: url + poke[2].toLowerCase() + ".png"
        });
        Object.assign(s3, {
          style: 'margin-left: 2px',
          src: url + poke[3].toLowerCase() + ".png"
        });
        Object.assign(s4, {
          style: 'margin-left: 2px',
          src: url + poke[4].toLowerCase() + ".png"
        });
        Object.assign(s5, {
          style: 'margin-left: 2px',
          src: url + poke[5].toLowerCase() + ".png"
        });
        a.appendChild(s0);
        a.appendChild(s1);
        a.appendChild(s2);
        a.appendChild(s3);
        a.appendChild(s4);
        a.appendChild(s5);
        z1.style.textAlign = "left"
        z1.appendChild(b);
        b.appendChild(document.createTextNode(title));
        z1.appendChild(auth)
        auth.appendChild(date);
        z1.insertBefore(saut, z1.appendChild(auth));
        z0.appendChild(a);
        document.getElementById("myTr" + [i]).appendChild(z0);
        document.getElementById("yourTr" + [i]).appendChild(z1);
        li.insertBefore(saut, x0);
     }
  }} catch (err) {
    console.error(err);
  }
}
Display().call