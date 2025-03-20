const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

const [[N], ...arr] = input;

const result = Array.from({ length: N + 1 }, () => 0);

for (let i = 0; i < N; i++) {
  const [t, p] = arr[i];

  result[i] = Math.max(result[i], result[i - 1] || 0);
  if (i + t <= N) result[i + t] = Math.max(result[i + t], result[i] + p);
}

console.log(Math.max(result[N], result[N - 1]));
