function solution(topping) {
  // 누적합 이용
  const left = new Array(10001).fill(0);
  const right = new Array(10001).fill(0);
  let leftCount = 0,
    rightCount = 0;
  let answer = 0;

  for (let i = 0; i < topping.length; i++) {
    if (left[topping[i]] === 0) leftCount += 1;
    left[topping[i]] += 1;
  }
  for (let i = topping.length - 1; i >= 0; i--) {
    left[topping[i]] -= 1;
    right[topping[i]] += 1;
    if (left[topping[i]] === 0) leftCount -= 1;
    if (right[topping[i]] === 1) rightCount += 1;
    if (leftCount === rightCount) answer += 1;
  }
  return answer;
}
