const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

// 몫이 1 이상이면 추가
// 나머지를 현재 금액으로 갱신

const getCountCoins = (money) => {
  let current = money;
  const coins = [25, 10, 5, 1];
  const result = [0, 0, 0, 0];
  for (let i = 0; i < 4; i++) {
    const coin = coins[i];
    if (current / coin >= 1) {
      result[i] = Math.floor(current / coin);
      current = current % coin;
    }
  }
  return result;
};

const N = input.splice(0, 1);
const numbers = input;
for (let i = 0; i < N; i++) {
  console.log(...getCountCoins(numbers[i]));
}
