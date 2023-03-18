//문제: 10480
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = input.shift();
  input.forEach((e) => {
    e % 2 === 0 ? console.log(`${e} is even`) : console.log(`${e} is odd`);
  });
}
