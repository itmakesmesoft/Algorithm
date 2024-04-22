function solution(k, tangerine) {
  var answer = 0;
  const dict = new Array(10000001).fill(0);
  tangerine.forEach((a) => (dict[a] += 1));
  dict.sort((a, b) => b - a);
  total = 0;
  for (let i = 0; i < dict.length; i++) {
    total += dict[i];
    answer += 1;
    if (total >= k) break;
  }
  return answer;
}
