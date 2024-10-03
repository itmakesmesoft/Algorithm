function solution(sizes) {
  const answer = [0, 0];
  for (let i = 0; i < sizes.length; i++) {
    const a = Math.max(...sizes[i]);
    const b = Math.min(...sizes[i]);
    answer[0] = Math.max(answer[0], a);
    answer[1] = Math.max(answer[1], b);
  }
  return answer[0] * answer[1];
}
