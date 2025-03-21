const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const N = Number(input);

const lst = Array.from({ length: N + 1 }).fill(true);
lst[0] = false;
lst[1] = false;

// 에라토스테네스의 체
for (let i = 2; i <= Math.floor(N ** 0.5); i++) {
  if (lst[i]) {
    let j = 2;
    while (i * j <= N) {
      lst[i * j] = false;
      j++;
    }
  }
}
const primes = lst
  .map((isPrime, i) => (isPrime ? i : -1))
  .filter((num) => num > 0);
// 누적합 구하기
const accumulative = [0];

let prev = 0;
for (let i = 0; i < primes.length; i++) {
  prev += primes[i];
  accumulative.push(prev);
}

// 투포인터
let start = 0;
let end = 1;
let count = 0;
while (start <= end && end < accumulative.length) {
  const total = accumulative[end] - accumulative[start];
  if (total > N) {
    start += 1;
  } else if (total < N) {
    end += 1;
  } else {
    count += 1;
    start += 1;
    end += 1;
  }
}

console.log(count);
