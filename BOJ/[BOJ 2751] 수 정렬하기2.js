const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
const [N, ...arr] = input;

const mergeSort = (arr) => {
  if (arr.length === 1) return arr;

  const mid = Math.floor(arr.length / 2);
  return merge(mergeSort(arr.slice(0, mid)), mergeSort(arr.slice(mid)));
};

const merge = (lst1, lst2) => {
  const result = [];
  let [i, j] = [0, 0];
  while (lst1.length > i && lst2.length > j) {
    if (lst1[i] >= lst2[j]) {
      result.push(lst2[j]);
      j++;
    } else {
      result.push(lst1[i]);
      i++;
    }
  }

  while (i < lst1.length) {
    result.push(lst1[i]);
    i++;
  }
  while (j < lst2.length) {
    result.push(lst2[j]);
    j++;
  }
  return result;
};

const answer = mergeSort(arr);

console.log(answer.join("\n"));
