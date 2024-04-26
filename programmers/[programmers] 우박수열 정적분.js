function solution(k, ranges) {
  var answer = [];
  function getArr(num) {
    const result = [num];
    while (num > 1) {
      if (num % 2 === 0) num = num / 2;
      else if (num % 2 === 1) num = num * 3 + 1;
      result.push(num);
    }
    return result;
  }
  const arr = getArr(k);
  const n = arr.length - 1;
  ranges.forEach((range) => {
    if (range[0] > n + range[1]) answer.push(-1);
    else if (range[0] === n + range[1]) answer.push(0);
    else {
      let total = 0;
      for (let i = range[0]; i < n + range[1]; i++) {
        total += (arr[i] + arr[i + 1]) / 2;
      }
      answer.push(total);
    }
  });

  return answer;
}
