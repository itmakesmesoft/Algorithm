t = int(input())
for case in range(1, t+1):
    n, m, k = map(int, input().split())
    customers = list(map(int, input().split()))
    bucket = [0]*11112
    for customer in customers: # 예약 손님 버킷에 담기
        bucket[customer]+=1
    for i in range(1, 11112):
        bucket[i]+=bucket[i-1]
    flag = 1
    for sec in customers:
        number = bucket[sec] # number = sec 초의 손님 숫자
        stock = (sec//m)*k #현재 갯수
        if number>stock:
            flag = 0
            break
    if flag:
        print(f"#{case} Possible")
    else:
        print(f"#{case} Impossible")