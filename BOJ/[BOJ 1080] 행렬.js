const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 문제 풀이

const [N, M] = input.splice(0, 1)[0].split(" ").map(Number);
const origin = input.splice(0, N).map((i) => i.split("").map(Number));
const tobe = input.map((i) => i.split("").map(Number));

const convertArr = (arr, startY, startX) => {
  const cloned = [...arr];
  for (let i = startY; i < startY + 3; i++) {
    for (let j = startX; j < startX + 3; j++) {
      cloned[i][j] = (cloned[i][j] + 1) % 2;
    }
  }
  return cloned;
};
let temp = [...origin];
let count = 0;
for (let i = 0; i < N - 2; i++) {
  for (let j = 0; j < M - 2; j++) {
    if (temp[i][j] !== tobe[i][j]) {
      temp = convertArr(temp, i, j);
      count += 1;
    }
  }
}

console.log(temp.join("") === tobe.join("") ? count : -1);
