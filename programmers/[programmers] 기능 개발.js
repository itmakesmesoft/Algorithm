function solution(progresses, speeds) {
  const rest = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );
  const answer = [];
  let count = 1;
  let maxNum = rest.shift();
  while (rest.length > 0) {
    const current = rest.shift();
    if (maxNum < current) {
      answer.push(count);
      maxNum = current;
      count = 1;
    } else {
      count += 1;
    }
  }
  answer.push(count);
  return answer;
}
