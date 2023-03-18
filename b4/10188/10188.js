//문제: 10188
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = input.shift();
  input.forEach((e, idx) => {
    const [column, row] = e.split(" ").map(Number);
    for (let i = 0; i < row; i++) {
      line = "";
      for (let j = 0; j < column; j++) {
        line += "X";
      }
      console.log(line);
    }
    if (idx != n - 1) console.log("");
  });
}
