function solution(priorities, location) {
  const sorted = [...priorities].sort((a, b) => b - a);
  const arr = Array.from({ length: priorities.length }, (v, i) => i);
  const answer = [];
  while (arr.length > 0) {
    const cur = arr.shift();
    if (priorities[cur] === sorted[0]) {
      sorted.shift();
      answer.push(cur);
    } else {
      arr.push(cur);
    }
  }
  return answer.indexOf(location) + 1;
}
