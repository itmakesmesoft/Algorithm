const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) =>
    v
      .replace("\r", "")
      .split(" ")
      .map((str) => Number(str))
  );

let maxCoordinate = [1, 1];
let maxNumber = -1;
for (let y = 0; y < 9; y++) {
  for (let x = 0; x < 9; x++) {
    if (input[y][x] > maxNumber) {
      maxNumber = input[y][x];
      maxCoordinate = [y + 1, x + 1];
    }
  }
}
console.log(maxNumber);
console.log(...maxCoordinate);
