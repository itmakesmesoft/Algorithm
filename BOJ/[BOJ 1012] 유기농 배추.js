const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = Number(input.splice(0, 1));

const BFS = (y, x, ground, visited, N, M) => {
  const q = [[y, x]];
  visited[y][x] = 1;
  const direct = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  while (q.length > 0) {
    const [y, x] = q.shift();
    for (let i = 0; i < 4; i++) {
      const ny = y + direct[i][0];
      const nx = x + direct[i][1];
      if (ny >= N || nx >= M || ny < 0 || nx < 0) continue;
      if (ground[ny][nx] === 0 || visited[ny][nx]) continue;
      visited[ny][nx] = 1;
      q.push([ny, nx]);
    }
  }
};

for (let i = 0; i < T; i++) {
  const [M, N, K] = input.splice(0, 1)[0].split(" ").map(Number);
  const lst = input.splice(0, K).map((v) => v.split(" ").map(Number));
  const ground = Array.from({ length: N }).map(() =>
    Array.from({ length: M }).fill(0)
  );
  const visited = JSON.parse(JSON.stringify(ground));

  for (const [x, y] of lst) ground[y][x] = 1;
  let count = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (ground[i][j] === 1 && visited[i][j] === 0) {
        BFS(i, j, ground, visited, N, M);
        count += 1;
      }
    }
  }
  console.log(count);
}
