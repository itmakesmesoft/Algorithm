// const fs = require("fs");
// const input = fs
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((item) => item.split(" ").map(Number));

// const input = `15 15
// 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15
// 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14
// 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13
// 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12
// 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11
// 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10
// 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9
// 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8
// 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7
// 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6
// 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5
// 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4
// 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3
// 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2
// 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1`
//   .trim()
//   .split("\n")
//   .map((item) => item.split(" ").map(Number));
// const [[M, N], ...arr] = input;

// const BFS = (y, x) => {
//   const q = [[y, x, arr[y][x]]];
//   const direct = [
//     [0, 1],
//     [0, -1],
//     [1, 0],
//     [-1, 0],
//   ];
//   let count = 0;

//   while (q.length > 0) {
//     const [curY, curX, prev] = q.shift();
//     if (curY === M - 1 && curX === N - 1) {
//       count += 1;
//       continue;
//     }
//     if (arr[curY][curX] < arr[M - 1][N - 1]) continue;
//     for (const weight of direct) {
//       const ny = curY + weight[0];
//       const nx = curX + weight[1];
//       if (ny >= M || nx >= N || ny < 0 || nx < 0) continue;
//       if (arr[ny][nx] >= prev) continue;
//       q.push([ny, nx, arr[ny][nx]]);
//     }
//   }
//   return count;
// };

// console.log(BFS(0, 0));
