//
// 문제 2. 주어진 NxN격자가 비밀 메시지 패턴(사토르 마방진)을 따르는지 확인하는 함수 제작

// - 비밀패턴: 어떤 방향으로 읽어도 동일한 내용을 가져야 함
// - solution함수는 N개의 문자열을 요소로 갖는 배열을 첫 번째 인자로 받음
// - 배열의 각 요소는 모두 길이가 N인 문자열
// - 이 격자가 비밀 메시지 패턴을 따를 경우 true, 그렇지 않을 경우 false를 반환

// 예시 입출력
// solution(["WOW", "OEO", "WOW"]); // true
// solution(["HEL", "LOO", "OLE"]); // false
// solution(["SATOR", "AREPO", "TENET", "OPERA", "ROTAS"]); // true
// solution(["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY"]); // false
// ;

function solution(arr) {
  return isSator(arr);
}
function isSator(arr) {
  for (let y = 0; y < arr.length; y++) {
    for (let x = 0; x < arr[y].length; x++) {
      if (arr[y][x] !== arr[x][y]) return false;
    }
  }
  return true;
}

console.log(solution(["WOW", "OEO", "WOW"]));
console.log(solution(["HEL", "LOO", "OLE"]));
console.log(solution(["SATOR", "AREPO", "TENET", "OPERA", "ROTAS"]));
console.log(solution(["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY"]));
