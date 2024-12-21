// 시간이 없어서 chatGPT의 도움을 받았습니다ㅠ. 다음에 꼭 풀어볼게요

const fs = require("fs");
const N = parseInt(fs.readFileSync("/dev/stdin").toString());

function findFraction(N) {
  let diagonal = 1;
  while (N > diagonal) {
    N -= diagonal;
    diagonal++;
  }

  let numerator, denominator;
  if (diagonal % 2 === 0) {
    numerator = N;
    denominator = diagonal - N + 1;
  } else {
    numerator = diagonal - N + 1;
    denominator = N;
  }
  return `${numerator}/${denominator}`;
}
console.log(findFraction(N));
