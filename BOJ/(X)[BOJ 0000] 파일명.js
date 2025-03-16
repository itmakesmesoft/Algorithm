const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

// 문제 풀이

const [[N, K], ...arr] = input;
arr.sort((a, b) => a[0] - b[0]);
arr.unshift([0, 0]);

const dp = Array.from({ length: N + 1 }, () =>
  Array.from({ length: K + 1 }).fill(0)
);

for (let i = 1; i < N + 1; i++) {
  const [W, V] = arr[i];
  for (let j = 1; j <= K; j++) {
    if (j - W >= 0) dp[i][j] = Math.max(dp[i - 1][j - W] + V, dp[i - 1][j]);
    else dp[i][j] = dp[i - 1][j];
  }
}
console.log(dp[N][K]);
