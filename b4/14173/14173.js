//문제: 14173
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [a, b, c, d] = input[0].split(" ").map(Number);
  const [a1, b1, c1, d1] = input[1].split(" ").map(Number);
  const arr1 = [a, c, a1, c1].sort((a, b) => a - b);
  const arr2 = [b, d, b1, d1].sort((a, b) => a - b);
  let e = arr1[3] - arr1[0];
  let f = arr2[3] - arr2[0];
  e > f ? console.log(e * e) : console.log(f * f);
}
