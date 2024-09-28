function solution(n, times) {
  function getTotal(num) {
    return times.reduce((total, cur) => total + Math.floor(num / cur), 0);
  }

  let start = 0,
    end = Math.max(...times) * n;

  while (start <= end) {
    const mid = Math.round((start + end) / 2);
    const result = getTotal(mid);
    if (result >= n) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return start;
}
