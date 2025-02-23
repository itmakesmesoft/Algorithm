const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

const [[V, E], ...lst] = input;
const arr = Array.from({ length: V }, () =>
  Array.from({ length: V }, () => Infinity)
);

for (let [a, b, c] of lst) {
  arr[a - 1][b - 1] = c;
}

// 플로이드 워셜로 접근
for (let v = 0; v < V; v++) {
  for (let i = 0; i < V; i++) {
    for (let j = 0; j < V; j++) {
      arr[i][j] = Math.min(arr[i][j], arr[i][v] + arr[v][j]);
    }
  }
}
let minimum = Infinity;
for (let i = 0; i < V; i++) {
  minimum = Math.min(minimum, arr[i][i]);
}
console.log(minimum === Infinity ? -1 : minimum);
