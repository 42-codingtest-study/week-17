//문제: 11121
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  input.shift();
  input.forEach((e) => {
    e.split(" ")[0] === e.split(" ")[0]
      ? console.log("OK")
      : console.log("ERROR");
  });
}
