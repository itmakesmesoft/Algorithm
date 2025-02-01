const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [N, r, c] = input;

let total = 0;
const recur = (n, r, c) => {
  const k = 2 ** (n - 1);
  if (n === 0) {
    return;
  }
  if (r < k && c < k) {
  } else if (r < k && c >= k) {
    total += k ** 2;
  } else if (r >= k && c < k) {
    total += k ** 2 * 2;
  } else if (r >= k && c >= k) {
    total += k ** 2 * 3;
  }
  recur(n - 1, r % k, c % k);
};
recur(N, r, c);
console.log(total);
