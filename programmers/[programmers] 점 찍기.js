function solution(k, d) {
  var answer = 0;
  let a = 0,
    b = d;

  while (a <= d && b >= 0) {
    const curD = (a ** 2 + b ** 2) ** 0.5;
    if (curD > d) {
      b -= 1;
    } else {
      answer += parseInt(b / k + 1);
      a += k;
    }
  }
  return answer;
}
