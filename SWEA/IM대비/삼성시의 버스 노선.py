t = int(input())
for case in range(1, t+1):
    n = int(input())
    buses = [list(map(int, input().split())) for _ in range(n)] # 테스트 케이스
    p = int(input())
    stops = [int(input()) for _ in range(p)] # 정류장
    result = [0]*p #결과를 담을 리스트 생성
    for j in range(p):
        for i in range(n):
            if buses[i][0] <= stops[j] and buses[i][1] >= stops[j] :
                result[j]+=1
    print(f"#{case}", end=' ') # 출력
    for i in range(p):
        print(f'{result[i]}', end = ' ')
    print()

'''
test case

2
4
1 4
1 5
1 4
1 2
1
2
3
4
5
4
1 4
1 5
1 4
1 2
5
1
2
3
4
5

'''