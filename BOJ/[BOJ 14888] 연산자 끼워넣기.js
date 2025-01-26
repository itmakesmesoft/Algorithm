const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input.splice(0, 1));
const arr = input[0].split(" ").map(Number);
const restOperators = input[1].split(" ").map(Number);

let maxTotal = -1 * Infinity;
let minTotal = Infinity;

const operate = (current, num, idx) => {
  switch (idx) {
    case 0:
      return current + num;
    case 1:
      return current - num;
    case 2:
      return current * num;
    case 3:
      if (current === 0) return 0;
      if (current < 0) return Math.floor(Math.abs(current) / num) * -1;
      return Math.floor(current / num);
  }
};

const getResult = (index, current) => {
  if (index === N) {
    if (restOperators.reduce((t, i) => t + i) === 0) {
      if (current > maxTotal) {
        maxTotal = current;
      }
      if (current < minTotal) {
        minTotal = current;
      }
    }
    return;
  }

  for (let i = 0; i < 4; i++) {
    if (restOperators[i] > 0) {
      restOperators[i] -= 1;
      getResult(index + 1, operate(current, arr[index], i));
      restOperators[i] += 1;
    }
  }
};

getResult(1, arr[0]);
console.log(maxTotal === 0 ? Math.abs(maxTotal) : maxTotal);
console.log(minTotal === 0 ? Math.abs(minTotal) : minTotal);
