const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let x = 0;
let result = "";
while (true) {
  let flag = true;
  for (let y = 0; y < input.length; y++) {
    if (input[y].length <= x) continue;
    result += input[y][x];
    flag = false;
  }
  x += 1;
  if (flag) break;
}
console.log(result);
