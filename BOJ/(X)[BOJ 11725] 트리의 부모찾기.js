// const fs = require("fs");
// const input = fs
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((item) => item.split(" ").map(Number));
// // const input = `7
// // 1 6
// // 6 3
// // 3 5
// // 4 1
// // 2 4
// // 4 7`
// //   .trim()
// //   .split("\n")
// //   .map((item) => item.split(" ").map(Number));
// const [[N], ...lst] = input;

// const memo = Array.from({ length: N + 1 }).fill(-1);
// const arr = Array.from({ length: N + 1 }).map(() => []); // 인접행렬
// let flag;
// const answer = [];

// const bfs = (start) => {
//   const q = [[start, -1]];
//   const visited = Array.from({ length: N }).fill(false);

//   while (q.length > 0) {
//     const [cur, parent] = q.shift();
//     if (cur === 1) return parent;
//     for (const num of arr[cur]) {
//       if (visited[num]) continue;
//       visited[num] = true;
//       q.push([num, parent > 0 ? parent : num]);
//     }
//   }
// };

// // 1. 인접행렬 만들기
// for (const [st, ed] of lst) {
//   arr[st].push(ed);
//   arr[ed].push(st);
// }

// // 2. 2번부터 순회하며, root정보 수집
// for (let i = 2; i < N + 1; i++) {
//   const res = bfs(i);
//   answer.push(res);
// }

// console.log(answer.join("\n"));

// 아래는 구글링한 풀이법

const [N, ...edges] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const graph = Array.from({ length: +N + 1 }).map(() => []);
const checked = Array.from({ length: +N + 1 }).fill(false);
const parentNodes = Array.from({ length: +N + 1 }).fill(null);

edges.forEach((edge) => {
  const [start, end] = edge.split(" ");

  graph[start].push(+end);
  graph[end].push(+start);
});

const dfsSearchForParent = (vertex) => {
  if (checked[vertex]) return;

  checked[vertex] = true;

  graph[vertex].forEach((child) => {
    if (!checked[child]) parentNodes[child] = vertex;

    dfsSearchForParent(child);
  });
};

dfsSearchForParent(1);

let answer = "";

for (let i = 2; i < parentNodes.length; i++) {
  answer += parentNodes[i] + "\n";
}

console.log(answer);
