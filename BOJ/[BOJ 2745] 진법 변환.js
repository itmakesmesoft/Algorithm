const fs = require("fs");
const [N, B] = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const len = N.length;
let result = 0;
// 0~9 : 48~57
// A~Z : 65~90
for (let i = 0; i < len; i++) {
  const index = parseInt(N[len - i - 1].charCodeAt());
  // 문자인 경우 A(65)에서 10을 뺸 55을 뺴기
  const number = index >= 65 ? index - 55 : index - 48;
  result += number * B ** i;
}

console.log(result);
