const fs = require("fs");
const N = Number(fs.readFileSync("/dev/stdin").toString().trim());

// 1. 5의 몫과 나머지 구하기 -> dividerByFive
// 2. 5의 나머지(restByFive)를 3으로 나눈 나머지(restByThree)가 0 -> 정답 (dividerByFive + dividerByThree)
// 3.     나머지(restByFive)를 3으로 나눈 나머지(restByThree)가 0이 아니면 5의 dividerByFive-1 후 다시 1로

let dividerByFive = Math.floor(N / 5);
let dividerByThree = 0;
while (dividerByFive >= 0) {
  const restByFive = N - 5 * dividerByFive;
  if (restByFive % 3 === 0) {
    dividerByThree = Math.floor(restByFive / 3);
    break;
  }
  dividerByFive -= 1;
}
console.log(dividerByFive + dividerByThree);
