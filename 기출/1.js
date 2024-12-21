// 문제1 : 주어진 값이 비어있는지 검사하는 함수 제작

// 조건
// 1. 객체의 모든 속성 값이 비어있거나, 속성 자체가 없으면 비어있다고 간주
// 2. 배열의 모든 요소가 비어있으면 비어있다고 간주
// 3. 원시 타입은 비어있지 않다고 간주
// 4. 빈 문자열은 비어있다고 간주
// 5. null 과 undefined는 비어있다고 간주. null과 undefined를 제외한 falsy value는 비어있지 않음

// 비어있는 경우 true, 비어있지 않은 경우 false 반환

// 예시
// solution(null) // true
// solution({}) // true
// solution(0) // false
// solution([{}, {a:[]}]) // true

function solution(value) {
  return isEmpty(value);
}

function isEmpty(value) {
  if (value === undefined || value === null) return true;
  if (typeof value === "string" && value !== "") return false;
  if (typeof value === "number") return false;
  if (Array.isArray(value)) {
    for (const val of value) {
      if (!isEmpty(val)) {
        return false;
      }
    }
    return true;
  }
  if (typeof value === "object") {
    for (const key of Object.keys(value)) {
      if (!isEmpty(key) && !isEmpty(value[key])) return false;
    }
    return true;
  }
}

console.log(solution(null)); // true
console.log(solution({})); // true
console.log(solution(0)); // false
console.log(solution([{}, { a: [] }])); // true
console.log(solution([{ b: "c" }])); // false
