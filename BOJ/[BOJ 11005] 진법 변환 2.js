const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

let [N, B] = input.split(" ").map(Number);

let result = "";
while (N > 0) {
  const divider = parseInt(N / B);
  const rest = parseInt(N % B);
  if (rest >= 10) {
    result = String.fromCharCode(rest + 55) + result;
  } else {
    result = String(rest) + result;
  }
  N = divider;
}
console.log(result);
