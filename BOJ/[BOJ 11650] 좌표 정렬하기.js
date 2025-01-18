const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

input.splice(0, 1);
const arr = input.map((n) => n.split(" ").map(Number));

const sorted = arr.sort(([a1, a2], [b1, b2]) => a1 - b1 || a2 - b2);
console.log(sorted.map((n) => n.join(" ")).join("\n"));
