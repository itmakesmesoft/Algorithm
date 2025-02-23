const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

const [[N], ...[lst]] = input;

const stack = Array.from({ length: N }, (_, i) => i);
const result = Array.from({ length: N }, () => 0);
let i = 1;
for (const num of lst) {
  const index = stack.splice(num, 1)[0];
  result[index] = i;
  i += 1;
}

console.log(result.join(" "));
