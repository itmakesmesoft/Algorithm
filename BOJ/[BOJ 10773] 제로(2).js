const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

// 문제 풀이

const [K, ...lst] = input;
const stack = [];
for (const num of lst) {
  if (num === 0 && stack.length > 0) stack.pop();
  else stack.push(num);
}
console.log(stack.reduce((total, current) => total + current, 0));
