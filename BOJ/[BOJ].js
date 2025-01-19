const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const arr = inputs[1].split(" ").map(Number);
const sorted = Array.from(new Set(arr)).sort((a, b) => a - b);

// 이분탐색 활용해 인덱스 구하기

const binarySearch = (num) => {
  let start = 0;
  let end = sorted.length - 1;
  let mid;
  while (start <= end && sorted[mid] !== num) {
    mid = Math.floor((start + end) / 2);
    if (sorted[mid] > num) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return mid;
};

const result = [];
for (const num of arr) {
  result.push(binarySearch(num));
}

console.log(result.join(" "));
