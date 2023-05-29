// Onclick of the button
document.querySelector("button").onclick = function () {  
    url = document.getElementById("url").value
    eel.getepub(url)
  }