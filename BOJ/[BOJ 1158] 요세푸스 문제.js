const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

const [N, K] = input.map((n) => parseInt(n));
const arr = Array.from({ length: N }, (_, i) => i + 1);

const answer = [];
let currentIndex = K - 1;
while (arr.length > 0) {
  if (currentIndex > arr.length - 1) {
    const rest = Math.abs(currentIndex - arr.length) % arr.length;
    currentIndex = rest;
  } else {
    const [num] = arr.splice(currentIndex, 1);
    answer.push(num);
    currentIndex += K - 1;
  }
}
console.log(`<${answer.join(", ")}>`);
