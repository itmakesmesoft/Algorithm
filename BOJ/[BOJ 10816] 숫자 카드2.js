const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, _arr, M, _lst] = input;
const arr = _arr.split(" ").map(Number);
const lst = _lst.split(" ").map(Number);
const memo = Array.from({ length: 20000001 }).fill(0);
arr.forEach((v) => {
  memo[v + 10000000] += 1;
});
const answer = lst.map((v) => memo[v + 10000000]);
console.log(answer.join(" "));
