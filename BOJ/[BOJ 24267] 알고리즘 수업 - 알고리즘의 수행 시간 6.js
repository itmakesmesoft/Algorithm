const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const N = parseInt(input);
// 조합 이용 (nC3)
const result = (BigInt(N) * BigInt(N - 1) * BigInt(N - 2)) / BigInt(6);
console.log(String(result));
console.log(3);
