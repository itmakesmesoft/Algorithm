const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

const [N, M] = input.splice(0, 1)[0];
const arr = input.splice(0, 1)[0];
const lst = input;

// 누적합 구하기
const prefixSum = Array.from({ length: N }, () => 0);
let total = 0;
for (let i = 0; i < N; i++) {
  total += arr[i];
  prefixSum[i] = total;
}

// 구간합 구하기
const results = [];
for (const [i, j] of lst) {
  if (i > 1) {
    results.push(prefixSum[j - 1] - prefixSum[i - 2]);
  } else {
    results.push(prefixSum[j - 1]);
  }
}
console.log(results.join("\n"));
