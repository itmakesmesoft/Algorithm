const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const [M, N] = input.split("\n").map(Number);

const max = Math.max(M, N) + 1;
const bucket = Array.from({ length: max }).fill(true);
bucket[0] = false;
bucket[1] = false;

for (let i = 0; i <= max; i++) {
  if (bucket[i]) {
    // console.log(i)
    let j = 2;
    while (i * j < max) {
      bucket[i * j] = false;
      j++;
    }
  }
}
const result = [];
for (let i = M; i <= N; i++) {
  if (bucket[i]) result.push(i);
}
if (result.length > 0) {
  console.log(result.reduce((prev, cur) => prev + cur));
  console.log(result[0]);
} else {
  console.log(-1);
}
