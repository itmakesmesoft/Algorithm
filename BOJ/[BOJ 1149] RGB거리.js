const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

const [[N], ...arr] = input;
const result = Array.from({ length: N }, () => [0, 0, 0]);

result[0] = [...arr[0]];

for (let i = 1; i < N; i++) {
  result[i][0] = arr[i][0] + Math.min(result[i - 1][1], result[i - 1][2]);
  result[i][1] = arr[i][1] + Math.min(result[i - 1][0], result[i - 1][2]);
  result[i][2] = arr[i][2] + Math.min(result[i - 1][0], result[i - 1][1]);
}
console.log(Math.min(...result[N - 1]));
