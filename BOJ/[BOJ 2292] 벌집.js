const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
const N = parseInt(input);
k = 1;
while (N > 3 * k * (k - 1) + 1) {
  k += 1;
}
console.log(k);
