const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input.splice(0, 1));
const half = N / 2;
const arr = input.map((item) => item.split(" ").map(Number));
const used = Array.from({ length: N }).fill(false);
const memo = {};
let minDiff = Infinity;

const getDiffScore = () => {
  let A = 0;
  let B = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (used[i] && used[j]) A += arr[i][j];
      else if (!used[i] && !used[j]) B += arr[i][j];
    }
  }
  return Math.abs(A - B);
};

const divide = (start, depth) => {
  if (depth === half) {
    const diff = getDiffScore();
    if (minDiff > diff) {
      minDiff = diff;
    }
    return;
  }

  for (let i = start; i < N; i++) {
    if (used[i]) continue;
    used[i] = true;
    divide(i + 1, depth + 1);
    used[i] = false;
  }
};

divide(0, 0);
console.log(minDiff);
