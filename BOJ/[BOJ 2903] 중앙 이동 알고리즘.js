// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString();
const input = 5;

const N = parseInt(input);
let prev = 2;
let current = 2;
for (let i = 1; i <= N; i++) {
  prev = current;
  current = 2 * prev - 1;
}
console.log(current ** 2);
