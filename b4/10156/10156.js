//문제: 10156
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [a, b, c] = input[0].split(" ").map(Number);
  a * b - c > 0 ? console.log(a * b - c) : console.log(0);
}
