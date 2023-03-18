//문제: 11257
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  input.shift();
  input.forEach((e) => {
    const [num, s, m, t] = e.split(" ").map(Number);
    let sum = s + m + t;
    if (sum >= 55 && s >= 10.5 && m >= 7.5 && t >= 12)
      console.log(`${num} ${sum} PASS`);
    else console.log(`${num} ${sum} FAIL`);
  });
}
