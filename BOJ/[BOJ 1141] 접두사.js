const fs = require("fs");
const arr = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(arr.splice(0, 1));

const isPrefix = (str1, str2) => {
  const len = Math.min(str1.length, str2.length);
  for (let i = 0; i < len; i++) {
    if (str1[i] !== str2[i]) return false;
  }
  return true;
};
const removed = Array.from({ length: N }).fill(false);
for (let i = 0; i < N; i++) {
  if (removed[i]) continue;
  for (let j = 0; j < N; j++) {
    if (i === j) continue;
    if (removed[j]) continue;
    if (isPrefix(arr[i], arr[j])) {
      const prefix = arr[i].length > arr[j].length ? j : i;
      removed[prefix] = true;
      break;
    }
  }
}
console.log(N - removed.reduce((tot, cur) => (cur ? tot + 1 : tot), 0));
