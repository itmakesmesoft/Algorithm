const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

const [[N], arr] = input;

// 오름차순 정렬
arr.sort((a, b) => a - b);

// 투포인터
let start = 0;
let end = N - 1;
let minimum = Infinity;
let mins = null;

while (start < end) {
  const sum = arr[start] + arr[end];

  if (Math.abs(sum) < minimum) {
    minimum = Math.abs(sum);
    mins = [arr[start], arr[end]];
  }
  if (sum > 0) {
    end -= 1;
  } else {
    start += 1;
  }
}

console.log(...mins);
