const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
inputs.splice(0, 1);

const getSumOfAscii = (str) => {
  const answer = str.split("").reduce((acc, cur) => {
    const code = String(cur.charCodeAt() - 96);
    return (acc += code.length === 1 ? "0" + code : code);
  }, "");
  return parseInt(answer);
};
const result = Array.from(
  new Set([...inputs.sort((a, b) => getSumOfAscii(a) - getSumOfAscii(b))])
);
console.log(result.join("\n"));
