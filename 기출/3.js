// 문제 : 숫자 읽기 쉽게 만드릭
// 숫자를 입력 받아 한국식 단위(만, 억, 조 등)를 사용하여 읽기 쉬운 형태로 변환하는 함수를 구현할 것

// 입력
// num: 변환할 숫자(문자열)
// maxKoreanUnitCount: 최대로 표시할 한국식 단위 수
// roundDownUnder1K: 1000 미만의 숫자를 반올림할지 여부(기본값 false)

// 요구사항
// 1. 숫자를 4자리씩 끊어 한국어 단위(만, 억, 조 등)을 표현해야 함
// 2. 각 다위 내에서는 3자리마다 쉼표(,)를 사용하여 구분해야 함
// 3. 음수도 처리할 수 있어야 함
// 4. 소수점 이하 숫자도 처리할 수 있어야 함
// 5. maxKoreanUnitCount에 따라 표시할 단위를 제한할 수 있어야 함
// 6. roundDownUnder1K가 true일 경우, 1000 미만의 숫자는 반올림해야 함
// 7. 불필요한 0 단위는 생략해야 함

// solution('1234567890', 1, false); // 12억
// solution('9876543210', 2, true);  // 98억 7,654만
// solution('123.456789', 5, false); // 123.456789

function solution(num, maxKoreanUnitCount, roundDownUnder1K = false) {
  const units = ["", "만", "억", "조", "경"];
  // 먼저 .점으로 구분 => 양의 정수만 판단, 소숫점은 나중에 표시
  const [strNumber, decimal] = num.split("."); // 0: 정수, 1: 소수점 이하
  let number = parseInt(strNumber);

  // 뒤에서부터 4자리마다 단위
  const numberArray = [];

  while (number > 0) {
    if (number > 9999) {
      if (roundDownUnder1K && numberArray.length === 0) {
        const num = number % 10000;
        const floor = Math.floor(num / 1000) * 1000;
        const under1K = Math.round((num % 1000) / 1000) * 1000;
        numberArray.unshift(floor + under1K);
      } else {
        numberArray.unshift(number % 10000);
      }
      number = Math.floor(number / 10000);
    } else {
      numberArray.unshift(number);
      break;
    }
  }
  let answer = "";
  for (let i = 0; i < Math.min(maxKoreanUnitCount, numberArray.length); i++) {
    const unit = units[numberArray.length - i - 1];
    answer += `${addComma(numberArray[i])}${unit} `;
  }
  if (decimal) answer = `${answer.trim()}.${decimal}`;
  return answer.trim();
}

const addComma = (num) => {
  // 뒤에서부터 3자리마다 쉼표
  return String(num).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

console.log(solution("1234567890", 1, false)); // 12억
console.log(solution("9876543210", 2, true)); // 98억 7,654만
console.log(solution("123.456789", 5, false)); // 123.456789
console.log(solution("000067890", 5, true)); // 6만 8,000
