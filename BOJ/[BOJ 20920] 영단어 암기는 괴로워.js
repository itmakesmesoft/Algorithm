const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 1. 자주 나오는 단어일수록 앞에 배치한다.
// 2. 해당 단어의 길이가 길수록 앞에 배치한다.
// 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

const [N, M] = input.splice(0, 1)[0].split(" ").map(Number);
const filtered = input.filter((item) => item.length >= M);
const _map = new Map();
const keys = new Set(filtered);
const lst = [...keys];

for (let key of keys) {
  _map[key] = 0;
}

for (let item of filtered) {
  _map[item] += 1;
}

lst.sort((a, b) => {
  if (_map[b] > _map[a]) return 1;
  else if (_map[b] === _map[a]) {
    if (b.length > a.length) return 1;
    else if (b.length === a.length) {
      if (b < a) return 1;
      else return -1;
    } else return -1;
  } else return -1;
});

console.log(lst.join("\n"));
