const keyrow1 = [
  "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
];
const keyrow2 =
  ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
const keyrow3 =
  ["submit", "z", "x", "c", "v", "b", "n", "m", "backspace"]

let createKeyboard = () => {
  let keyboardDiv = document.getElementById("keyboard")
  for (let i = 0; i < 3; i++) {
    let row = document.createElement("div")
    let keyrow
    row.className = "row"
    keyboardDiv.appendChild(row)
    //adding an elegant way to add the keys into rows
    if (i == 0) {
      keyrow = keyrow1;
    }
    else if (i == 1) {  
      keyrow = keyrow2;
    }
    else if (i == 2) {
      keyrow = keyrow3;
    }
    for (let j = 0; j < keyrow.length; j++) {
      key = keyrow[j];
      console.log(key);
      let btn = document.createElement("button");
      btn.innerHTML = key;
      if ((j == 0 | j == 8) && i == 2) {
        btn.className = "longerKeyboardKey"
      }
      else {
        btn.className = 'keyboardKey'
      }
      row.appendChild(btn);
    }
  }
}

document.addEventListener('loadKeyboard', createKeyboard())
