const fs = require("fs");
const [N, ...arr] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const sorted = arr.sort((a, b) => b - a);
let answer = -1;
for (let i = 0; i < N - 2; i++) {
  if (sorted[i] < sorted[i + 1] + sorted[i + 2]) {
    answer = sorted[i] + sorted[i + 1] + sorted[i + 2];
    break;
  }
}
console.log(answer);
