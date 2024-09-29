function solution(maps) {
  const N = maps.length,
    M = maps[0].length;
  const BFS = (y, x) => {
    const d = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];
    const visited = Array.from({ length: N }, () => Array(M).fill(false));
    const q = [[y, x, 1]];
    visited[y][x] = true;

    while (q.length > 0) {
      const [y, x, cnt] = q.shift();
      if (y === N - 1 && x === M - 1) {
        return cnt;
      }
      for (let i = 0; i < 4; i++) {
        const ny = y + d[i][0];
        const nx = x + d[i][1];
        if (ny >= N || nx >= M || ny < 0 || nx < 0) continue;
        if (visited[ny][nx] === true) continue;
        if (maps[ny][nx] === 1) {
          visited[ny][nx] = true;
          q.push([ny, nx, cnt + 1]);
        }
      }
    }
    return -1;
  };
  return BFS(0, 0, 0);
}
