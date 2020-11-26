const tagContainer = document.querySelector('.tag-container');
const input = document.querySelector('.tag-container input');
let tags = [];
var tag = null

document.getElementById("demo").innerHTML = "#" ;

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
    filter = "|" + item.toUpperCase() + "|";
    ul = document.getElementById("myMenu");
    li = ul.getElementsByTagName("li");
    document.getElementById("demo").innerHTML = "#" + tags;
    for (i = 0; i < li.length; i++) {
        //a = li[i].getElementsByTagName("a")[0];
        //txtValue = a.textContent || a.innerText;
        txtValue = li[i].getAttribute("tags");
        console.log(txtValue)
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
  console.log(e.target.tagName);
  if (e.target.tagName === 'I') {
    const tagLabel = e.target.getAttribute('data-item');
    const index = tags.indexOf(tagLabel);
    tags = [...tags.slice(0, index), ...tags.slice(index+1)];
    addTags();
    tag = tagLabel;
    tags.forEach(myFunction);
  }
})

input.focus();

