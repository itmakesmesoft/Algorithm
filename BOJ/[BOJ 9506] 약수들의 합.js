const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const isPerfect = (num) => {
  const result = [1];
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      result.push(i);
    }
  }
  const total =
    result.length > 0 ? result.reduce((prev, cur) => prev + cur) : 0;

  if (total == num) return `${num} = ${result.join(" + ")}`;
  return `${num} is NOT perfect.`;
};

for (const num of input) {
  if (num === -1) break;
  console.log(isPerfect(num));
}
