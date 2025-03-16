const fs = require("fs");
const N = Number(fs.readFileSync("/dev/stdin").toString().trim());

let i = 0;
while (2 ** i < N) i += 1;

const K = 2 ** i;

let divide = 0,
  start = 0,
  end = K;

if (N === K) console.log(K, 0);
else {
  while (start <= end && end > 0) {
    divide += 1;
    mid = Math.floor((start + end) / 2);
    if (mid < N) {
      start = mid;
    } else if (mid > N) {
      end = mid + 1;
    } else {
      console.log(K, divide);
      break;
    }
  }
}
