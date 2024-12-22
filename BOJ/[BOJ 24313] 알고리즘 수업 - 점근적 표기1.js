const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [a1, a0] = input[0].split(" ").map(Number);
const [c, n0] = input.slice(1).map(Number);

console.log(c >= a1 && a0 / (c - a1) <= n0 ? 1 : 0);
