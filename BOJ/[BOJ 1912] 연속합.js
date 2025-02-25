const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map(Number));

const [[N], ...[arr]] = input;
const accArr = Array.from({ length: N }, () => 0);
const result = Array.from({ length: N }, () => 0);
let startIndex = -1;
for (let i = 0; i < N; i++) {
  accArr[i] = i === 0 ? arr[i] : accArr[i - 1] + arr[i];
}

for (let i = 0; i < N; i++) {
  if (accArr[i] < 0) {
    if (startIndex < 0 || accArr[startIndex] > accArr[i]) {
      startIndex = i;
    }
  }
  if (i > 0) {
    if (i === startIndex) {
      result[i] = Math.max(accArr[i], arr[i], result[i - 1]);
    } else {
      result[i] =
        startIndex > -1
          ? Math.max(accArr[i] - accArr[startIndex], result[i - 1], arr[i])
          : Math.max(accArr[i], result[i - 1], arr[i]);
    }
  } else {
    result[i] = accArr[i];
  }
}
console.log(result[N - 1]);
