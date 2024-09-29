function solution(n, computers) {
  const N = computers.length,
    M = computers[0].length;
  const visited = Array(N).fill(false);
  let count = 0;

  const DFS = (prevY) => {
    for (let i = 0; i < M; i++) {
      if (visited[i] === true) continue;
      if (computers[prevY][i] === 0 || prevY === i) continue;
      visited[i] = true;
      DFS(i);
    }
  };

  for (let i = 0; i < N; i++) {
    if (visited[i] === true) continue;
    count += 1;
    DFS(i);
  }
  return count;
}
