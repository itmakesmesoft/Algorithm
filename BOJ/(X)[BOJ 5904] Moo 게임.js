// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim();
// const N = Number(input);

// 'm'과 'm' 사이의 인덱스를 담은 배열 만들기
//   const arr = [0];
//   let curIndex = 1;
//   let k = 3;
//   let flag = false;
//   while (curIndex <= N || flag) {
//     for (const num of arr) {
//       curIndex += num;
//       if (curIndex === N) {
//         flag = true;
//         break;
//       } else if (curIndex > N) break;
//     }

//     curIndex += k;
//     if (curIndex === N) {
//       flag = true;
//       break;
//     } else if (curIndex > N) break;

//     arr.push(k);
//     k += 1;

//     // for (const num of arr) {
//     //   curIndex += num;
//     //   if (curIndex === N) {
//     //     flag = true;
//     //     break;
//     //   } else if (curIndex > N) break;
//     // }
//   }
//   if (N === 1) {
//     console.log("m");
//   } else {
//     console.log(flag ? "m" : "o");
//   }

// 구글링 참고했어요...
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
let N = Number(input);
let totalLength = 0;
let temp = 3;

while (true) {
  totalLength = totalLength * 2 + temp;
  if (totalLength >= N) break;
  temp++;
}

while (true) {
  let prevLength = ~~((totalLength - temp) / 2);

  if (N <= prevLength) {
    totalLength = prevLength;
    temp--;
  } else if (prevLength < N && N <= prevLength + temp) {
    if (N - prevLength === 1) console.log("m");
    else console.log("o");
    break;
  } else if (prevLength + temp < N) {
    N -= prevLength + temp;
    totalLength = prevLength;
    temp--;
  }
}
