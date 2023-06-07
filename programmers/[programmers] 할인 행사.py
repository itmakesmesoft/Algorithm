def solution(want, number, discount):
    answer = 0
    # 사야할 목록이 모두 충족된 경우를 판단하는 함수
    def is_possible():
        for item in want:
            if itemlist[item]>0:
                return False
        return True

    # 가능한 경우 -> 모두 할인받을 수 있는 회원 등록 날짜의 총 일수를 반환 => 첫째날을 반환
    # 슬라이딩 윈도우 사용
    # 10일간 회원자격 부여 -> 윈도우의 길이 = 10
    # number 원소의 합은 항상 = 10
    # 내가 사야할 아이템 목록과 갯수
    itemlist = dict()
    for index, item in enumerate(want):
        itemlist[item]=number[index]

    # 먼저 0번부터 9번 인덱스까지 계산
    for i in range(0, 10):
        if discount[i] in itemlist:
            itemlist[discount[i]]-=1

    if is_possible():# 여기서 먼저 검증
        answer += 1
    # 1번부터 11, 2번부터 12.... k번부터 k+9번까지 검증
    for i in range(1, len(discount)-9):
        if discount[i-1] in itemlist:
            itemlist[discount[i-1]]+=1
        if discount[i+9] in itemlist:
            itemlist[discount[i+9]]-=1
        if is_possible():
            answer += 1

    # 가능한 날이 없는 경우 -> 0 반환
    return answer