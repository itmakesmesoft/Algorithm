function solution(order) {
  const stack = [];
  let orderIdx = 0;
  let curidx = 1;
  while (curidx <= order.length) {
    stack.push(curidx);
    while (stack.length > 0 && order[orderIdx] === stack[stack.length - 1]) {
      stack.pop();
      orderIdx++;
    }
    curidx++;
  }
  return orderIdx;
}

// 내 초기 코드
// function solution(order) {
//   let temp = []
//   let result = 0
//   let flag = false;
//   let i = 1
//   const maximum = order.length
//   while (order.length > 0) {
//       if (flag) break
//       console.log(i, order[0])
//       if (i === order[0]) {
//           result += 1
//           order.shift()
//           i+=1
//       } else if (order[0] > i) {
//           temp.push(i)
//           i+=1
//       } else {
//           while (temp.length>0) {
//               const j = temp.pop();
//               console.log(order, temp, i, j, result, flag)
//               if (j===order[0]) {
//                   result += 1
//                   order.shift()
//               } else {
//                   break
//               }
//           }
//       }
//   }
//   return result;
// }
