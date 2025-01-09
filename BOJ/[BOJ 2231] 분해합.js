const fs = require("fs");
const N = Number(fs.readFileSync("/dev/stdin").toString().trim());

const getM = (n) => {
  const str = typeof n === "number" ? String(n) : n;
  const tot = str.split("").reduce((total, s) => total + Number(s), 0);
  return tot + n;
};

let answer = 0;
for (let i = 1; i <= 1000000; i++) {
  if (getM(i) === N) {
    answer = i;
    break;
  }
}
console.log(answer);
