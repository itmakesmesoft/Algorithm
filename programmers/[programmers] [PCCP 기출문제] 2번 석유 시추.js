function solution(land) {
  const N = land.length,
    M = land[0].length;
  const visited = Array.from(Array(N), () => new Array(M).fill(0));
  const result = new Array(M).fill(0);
  const direct = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  function bfs(y, x) {
    const q = [];
    const usedRow = new Array(M).fill(0);
    let area = 1;
    q.push([y, x]);
    while (q.length > 0) {
      const [y, x] = q.shift();
      usedRow[x] = 1;
      for (let i = 0; i < 4; i++) {
        const ny = y + direct[i][0],
          nx = x + direct[i][1];
        if (ny > N - 1 || ny < 0 || nx > M - 1 || nx < 0) continue;
        if (visited[ny][nx] === 1) continue;
        if (land[ny][nx] === 0) continue;
        visited[ny][nx] = 1;
        q.push([ny, nx]);
        area += 1;
      }
    }
    for (let k = 0; k < M; k++) {
      if (usedRow[k] === 1) result[k] += area;
    }
  }

  for (let y = 0; y < N; y++) {
    for (let x = 0; x < M; x++) {
      if (land[y][x] === 1 && visited[y][x] === 0) {
        visited[y][x] = 1;
        bfs(y, x);
      }
    }
  }
  return Math.max(...result);
}
