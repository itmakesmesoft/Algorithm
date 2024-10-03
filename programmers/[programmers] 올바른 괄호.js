function solution(s) {
  const arr = s.split("");
  const stack = [];
  let flag = true;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "(") {
      stack.push(arr[i]);
    } else {
      if (stack.length === 0) {
        flag = false;
        break;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length > 0 ? false : flag;
}
