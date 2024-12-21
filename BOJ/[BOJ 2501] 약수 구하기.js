const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
const [N, K] = input.split(" ").map(Number);

const result = [];
for (let i = 1; i <= N; i++) {
  if (N % i === 0) result.push(i);
}
console.log(result.length > K - 1 ? result[K - 1] : 0);
