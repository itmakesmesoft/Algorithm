const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const k = input[0];
const arr = input.splice(1, input.length - 1);
const stack = [];

for (const num of arr) {
  if (num == 0) {
    stack.pop();
  } else {
    stack.push(parseInt(num));
  }
}
console.log(stack.reduce((tot, cur) => tot + cur, 0));
