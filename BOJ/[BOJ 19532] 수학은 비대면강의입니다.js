const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [a, b, c, d, e, f] = input;
const x = (f * b - c * e) / (b * d - a * e);
const y = (f * a - c * d) / (a * e - b * d);
console.log(parseInt(x), parseInt(y));
