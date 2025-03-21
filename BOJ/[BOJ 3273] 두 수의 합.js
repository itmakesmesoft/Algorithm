const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

const [[N], arr, [X]] = input;

// 오름차순 정렬
arr.sort((a, b) => a - b);

if (N == 1) console.log(0);
else {
  // 투포인터
  let start = 0;
  let end = N - 1;
  let count = 0;

  while (start < end) {
    const sum = arr[start] + arr[end];

    if (sum > X) {
      end -= 1;
    } else if (sum < X) {
      start += 1;
    } else {
      count += 1;
      start += 1;
      end -= 1;
    }
  }
  console.log(count);
}
