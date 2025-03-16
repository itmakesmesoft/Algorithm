const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" "));

const N = Number(input.splice(0, 1));
const arr = input.map((i) => i.map((j) => Math.max(j.charCodeAt() - 65, -1)));
arr.sort((a, b) => a[0] - b[0]);
const used = Array.from({ length: N }, () => false);
let forward = "";
let center = "";
let backward = "";

const dfs = (cur) => {
  const alphabet = String.fromCharCode(cur + 65);
  forward += alphabet;
  if (arr[cur][1] > -1) dfs(arr[cur][1]);
  center += alphabet;
  if (arr[cur][2] > -1) dfs(arr[cur][2]);
  backward += alphabet;
};
dfs(0);
console.log(forward, center, backward);
