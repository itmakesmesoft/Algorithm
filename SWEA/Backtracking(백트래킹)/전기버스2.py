from collections import deque

t = int(input())
for case in range(1, t+1):
    stops = list(map(int, input().split()))
    n, stops = stops[0], stops[1:]
    inf = int(21e8)
    result = [inf]*n # 각 충전소 별 최소의 충전횟수를 담을 배열 초기화
    q = deque()
    q.append([0, 0]) #index, count
    while q:
        index, count = q.popleft()
        if index == n-1: break
        for i in range(stops[index]):
            next = index+i+1
            if next>=len(result): continue
            if result[next] >= count:
                result[next] = count
                q.append([next, count+1])
    print(f'#{case} {result[n-1]}')
        
'''
test case

3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''