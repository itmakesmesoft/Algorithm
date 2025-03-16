// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input = `5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN`.split("\n");

const N = Number(input.splice(0, 1));
const result = Array.from({ length: N }, () => 0);

for (let i = 0; i < N; i++) {
  for (let via = 0; via < N; via++) {
    if (i == via) continue;
    for (let j = 0; j < N; j++) {
      if (i == j || j == via) continue;
      if (input[i][j] == "N" && input[i][via] == "Y" && input[via][j] == "Y") {
        result[i] += 1;
      }
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = i; j < N; j++) {
    if (i == j) continue;
    if (input[i][j] === "Y") {
      result[i] += 1;
      result[j] += 1;
    }
  }
}
console.log(Math.max(...result));
