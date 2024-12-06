const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = inputs.splice(0, 1);
const answer = [];
const stack = [];

const methods = (orderValue) => {
  const [order, value] = orderValue.split(" ");
  switch (order) {
    case "push":
      stack.push(value);
      break;
    case "pop":
      answer.push(stack.length > 0 ? stack.pop() : -1);
      break;
    case "size":
      answer.push(stack.length);
      break;
    case "empty":
      answer.push(stack.length === 0 ? 1 : 0);
      break;
    case "top":
      answer.push(stack.length > 0 ? stack[stack.length - 1] : -1);
      break;
  }
};

for (const input of inputs) {
  methods(input);
}
console.log(answer.join("\n"));
