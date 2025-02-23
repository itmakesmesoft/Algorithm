const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input.splice(0, 1)[0].split(" ").map(Number);
const arr = input.splice(0, N).map((i) => i.split(" ").map(Number));
const lst = input.map((i) =>
  i
    .split(" ")
    .map(Number)
    .map((i) => i - 1)
);

// 누적합 배열 만들기
const prefixSum = Array.from({ length: N }, () =>
  Array.from({ length: N }).fill(0)
);

for (let i = 0; i < N; i++) {
  let total = 0;
  for (let j = 0; j < N; j++) {
    total += arr[i][j];
    prefixSum[i][j] = total;
  }
}

// 구간합 구하기
const results = [];
for (const [x1, y1, x2, y2] of lst) {
  let total = 0;
  for (let i = x1; i < x2 + 1; i++) {
    if (y1 > 0) {
      total += prefixSum[i][y2] - prefixSum[i][y1 - 1];
    } else {
      total += prefixSum[i][y2];
    }
  }
  results.push(total);
}

console.log(results.join("\n"));
