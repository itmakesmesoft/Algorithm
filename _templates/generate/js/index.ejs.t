---
to: <%= domain %>/[<%= domain %> 0000] 파일명.js
---

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

// 문제 풀이