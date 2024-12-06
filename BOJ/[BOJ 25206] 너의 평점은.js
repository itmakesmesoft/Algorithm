const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" "));

const grades = {
  "A+": 4.5,
  A0: 4,
  "B+": 3.5,
  B0: 3,
  "C+": 2.5,
  C0: 2,
  "D+": 1.5,
  D0: 1,
  F: 0,
};
let totalScore = 0; // 학점*평점의 합
let totalGrade = 0; // 학점의 총합
for (let subject of input) {
  const [_, s, g] = subject;
  if (g !== "P") {
    const score = parseInt(s);
    const grade = grades[g];
    totalGrade += score;
    totalScore += score * grade;
  }
}
console.log(totalScore / totalGrade);
