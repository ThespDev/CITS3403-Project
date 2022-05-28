const keyrow1 = [
  "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
];
const keyrow2 =
  ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
const keyrow3 =
  ["submit", "z", "x", "c", "v", "b", "n", "m", "back"]
const keyrow4 = [' ']
let input = document.getElementById('guesstxt');

let createKeyboard = () => {
  let keyboardDiv = document.getElementById("keyboard")
  for (let i = 0; i < 4; i++) {
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
    else if (i == 3) {
      keyrow = keyrow4;
    }
    for (let j = 0; j < keyrow.length; j++) {
      key = keyrow[j];
      console.log(key);
      let btn = document.createElement("button");
      btn.innerHTML = key;
      if (((j == 0 | j == 8) && i == 2) || i == 3)  {
        btn.className = "longerKeyboardKey"
      }
      else {
        btn.className = 'keyboardKey'
      }
      btn.addEventListener('click', function() {
        let key = this.innerHTML
        if (this.className == "longerKeyboardKey" && key !== ' ') {
          if (key !== "submit" && key !== ' ') {
            let val = input.value;
            val = val.slice(0, val.length - 1);
            input.value = val;
          }
        }
        else {
          console.log(key)
          input.value += key
        }
      })
      row.appendChild(btn);
    }
  }
  console.log("creating keyboard")
}


document.addEventListener('LoadKeyboard', createKeyboard())
