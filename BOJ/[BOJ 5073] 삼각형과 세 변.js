const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
const numbers = input.split("\n").map((item) => item.split(" ").map(Number));

for (const numArr of numbers.slice(0, numbers.length - 1)) {
  numArr.sort((a, b) => b - a);
  const [a, b, c] = numArr;
  if (a >= b + c) {
    console.log("Invalid");
  } else if (a === b && b === c) {
    console.log("Equilateral");
  } else if (a != b && b != c && a != c) {
    console.log("Scalene");
  } else {
    console.log("Isosceles");
  }
}
