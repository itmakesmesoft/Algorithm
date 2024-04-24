function solution(arrayA, arrayB) {
  function getCommonNumber(arr) {
    let gcd = 0;
    const minimum = arr.sort((a, b) => a - b)[0];
    for (let n = minimum; n >= 2; n--) {
      let flag = true;
      for (let j = 0; j < arr.length; j++) {
        if (arr[j] % n != 0) {
          flag = false;
          break;
        }
      }
      if (flag) return n;
    }
    return 0;
  }

  function isIndivisible(num, arr) {
    if (num === 0) return false;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] % num === 0) return false;
    }
    return true;
  }

  const commonA = getCommonNumber(arrayA),
    commonB = getCommonNumber(arrayB);
  const result = [];
  if (isIndivisible(commonA, arrayB)) result.push(commonA);
  if (isIndivisible(commonB, arrayA)) result.push(commonB);
  return result.length > 0 ? Math.max(...result) : 0;
}
