//문제: 10768
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [month, day] = [input[0], input[1]].map(Number);
  if (month === 2 && day === 18) console.log("Special");
  else if (month * 30 + day < 78) console.log("Before");
  else console.log("After");
}
