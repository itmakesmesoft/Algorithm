const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const [A, B, V] = input.split(" ");
console.log(Math.ceil((V - B) / (A - B)));
