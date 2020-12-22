async function myFunction() {
  try {
    const response = await fetch('data')
    const CSV = await response.text();
    //const response1 = await fetch("dexdata.json");
    //const json = await response1.json();
    const arrCSV = CSV.split('\n');
    const ul = document.getElementById("myMenu")
    for (var i = 0, len = arrCSV.length; i < len; i++) {
      var li = document.createElement("li");
      var x = document.createElement("TABLE");
      var y = document.createElement("TR");
      var y1 = document.createElement("TR"); 
      var z = document.createElement("TD");
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
      var indice = arrCSV[i].split(",");
      var team = indice[7]
      var team = team.replace("Urshifu-Rapid-Strike","urshifu-rapidstrike");
      var team = team.replace("Mega-X","megax");
      var team = team.replace("Mega-Y","megay");
      var team = team.replace("Ho-Oh","hooh");
      var tags = indice[8] + team;
      var poke = team.split("|");
      var title = "[" + indice[1].toUpperCase() + "] " + indice[5] + " by " + indice[4];
      var text = document.createTextNode("");
      var date = document.createTextNode("Ajoutée le " + indice[2] + " par " + indice[3]);
      var saut = document.createElement("BR");
      li.setAttribute("tags", tags);
      ul.appendChild(li);
      li.appendChild(saut);
      li.appendChild(x);
      y.setAttribute("id", "myTr" + [i]);
      y1.setAttribute("id", "yourTr" + [i]);
      x.appendChild(y);
      x.appendChild(y1);
      z.style.background = "rgba(102 , 136 , 170 , 0.40)"
      a.setAttribute("id", "a" + [i])
      a.setAttribute("href", indice[0]);
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
      z.appendChild(a);
      document.getElementById("myTr" + [i]).appendChild(z);
      document.getElementById("yourTr" + [i]).appendChild(z1);
      li.insertBefore(saut, x);
  }} catch (err) {
    console.error(err);
  }
}
myFunction().call