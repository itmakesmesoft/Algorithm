const fs = require("fs");
// const [_, ...arr] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const input = `8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1`
  .trim()
  .split("\n");
const N = Number(input.splice(0, 1));
const arr = input.map((item) => item.split(" ").map(Number));
let totalWhite = 0;
let totalBlue = 0;

const isPossible = (startY, startX, length) => {
  if (length === 1) return arr[startY][startX];

  const newLength = Math.floor(length / 2);
  let blue = 0;
  let white = 0;
  for (let i = 0; i < 2; i++) {
    for (let j = 0; j < 2; j++) {
      const res = isPossible(
        startY + i * newLength,
        startX + j * newLength,
        newLength
      );
      blue += Number(res === 1);
      white += Number(res === 0);
    }
  }
  if (length === N && (blue === 4 || white === 4)) {
    totalBlue += Math.floor(blue / 4);
    totalWhite += Math.floor(white / 4);
    return -1;
  }
  if (blue === 4) return 1;
  if (white === 4) return 0;
  totalBlue += blue;
  totalWhite += white;
  return -1;
};

isPossible(0, 0, N);
console.log(totalWhite);
console.log(totalBlue);
