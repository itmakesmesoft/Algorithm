def solution(book_time):
    def str_to_int(string):
        time = string.split(':')
        return int(time[0])*60 + int(time[1])

    answer = 0
    # 대실 시간 별 겹치는 시간 구하기
    # 퇴실 후 10분간 청소
    # list에는 퇴실시간만 기록
        # list[i]와 앞으로 들어오는 대실시간의 입실시간-10을 비교

    lst = []
    book_time.sort(key=lambda x:x[0], reverse=True)

    while book_time:
        cur = book_time.pop()
        for i in range(len(lst)):
            # 입실 가능한 경우
            if str_to_int(lst[i])<=str_to_int(cur[0])-10:
                lst[i]=cur[1]
                break
            # 입실 불가능한 경우
        else:
            lst.append(cur[1])

    return len(lst)