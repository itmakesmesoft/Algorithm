const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [_, ...rest] = input;
const list = rest.map((v) => v.trim().split(" ").map(Number));

let area = 0;
const paper = Array.from({ length: 100 }).map(() =>
  Array.from({ length: 100 }).fill(false)
);

const paintRect = (_x, _y) => {
  for (let y = _y; y < _y + 10; y++) {
    for (let x = _x; x < _x + 10; x++) {
      if (!paper[y][x]) {
        paper[y][x] = true;
        area += 1;
      }
    }
  }
};

for (const [x, y] of list) {
  paintRect(x, y);
}
console.log(area);
