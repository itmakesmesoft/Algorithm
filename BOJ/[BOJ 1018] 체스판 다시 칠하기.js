const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = input.slice(1).map((item) => item.split(""));

const getCountBlock = (y, x) => {
  let count = 0;
  for (let i = y; i < y + 8; i++) {
    for (let j = x; j < x + 8; j++) {
      if (i >= arr.length || j >= arr[0].length) continue;
      if ((i + j) % 2 === 0 && arr[i][j] === "W") count += 1;
      if ((i + j) % 2 === 1 && arr[i][j] === "B") count += 1;
    }
  }
  return Math.min(64 - count, count);
};

let minCount = Infinity;

for (let y = 0; y < N - 7; y++) {
  for (let x = 0; x < M - 7; x++) {
    const result = getCountBlock(y, x);
    if (result < minCount) {
      minCount = result;
    }
  }
}
console.log(minCount);
