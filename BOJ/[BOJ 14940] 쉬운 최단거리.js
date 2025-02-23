const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input.splice(0, 1)[0].split(" ").map(Number);
const arr = input.map((item) => item.split(" ").map(Number));

const bfs = (y, x) => {
  const q = [[y, x, 0]];
  const result = Array.from({ length: N }, () =>
    Array.from({ length: M }).fill(0)
  );
  const visited = Array.from({ length: N }, () =>
    Array.from({ length: M }).fill(0)
  );
  visited[y][x] = 1;

  const direct = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  while (q.length > 0) {
    const [y, x, distance] = q.shift();
    result[y][x] = distance;
    for (let i = 0; i < 4; i++) {
      const ny = y + direct[i][0];
      const nx = x + direct[i][1];

      if (ny > N - 1 || nx > M - 1 || ny < 0 || nx < 0) continue;
      if (arr[ny][nx] === 0) continue;
      if (visited[ny][nx]) continue;
      visited[ny][nx] = 1;
      q.push([ny, nx, distance + 1]);
    }
  }

  return result;
};

const getStartLocation = () => {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] === 2) return [i, j];
    }
  }
  return [0, 0];
};

const [startY, startX] = getStartLocation();
const result = bfs(startY, startX);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (arr[i][j] === 1 && result[i][j] === 0) result[i][j] = -1;
  }
}

console.log(result.map((item) => item.join(" ")).join("\n"));
