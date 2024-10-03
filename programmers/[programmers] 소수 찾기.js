function solution(numbers) {
  let answer = 0;
  const cards = numbers.split("");
  const used = Array(numbers.length).fill(false);
  const dict = Array(10000000).fill(true);
  const memo = new Set();
  dict[0] = false;
  dict[1] = false;

  for (let i = 2; i < dict.length ** 0.5; i++) {
    let k = 2;
    while (i * k <= 9999999) {
      dict[i * k] = false;
      k += 1;
    }
  }

  function isPrimeNumber(num) {
    return dict[num];
  }

  function dfs(depth, cur) {
    const num = Number(cur);
    if (isPrimeNumber(num) && !memo.has(num)) {
      answer += 1;
      memo.add(num);
    }
    if (depth === numbers.length) return;
    for (let i = 0; i < numbers.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      dfs(depth + 1, cur + numbers[i]);
      used[i] = false;
    }
  }
  dfs(0, "");
  return answer;
}
