//문제: 11282
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const answer = String.fromCharCode(+input[0] + 44031);

  console.log(answer);
}
