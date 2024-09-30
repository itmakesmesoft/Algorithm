function solution(arr) {
  const answer = [arr[0]];
  if (arr.length <= 1) return answer;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] != arr[i]) answer.push(arr[i]);
  }
  return answer;
}
