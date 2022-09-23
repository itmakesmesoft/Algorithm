'''
1     
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''
from collections import deque

t = int(input())
for case in range(1, t+1):
    n, m, k = map(int, input().split()) # n 셀의 갯수, m 격리 시간, k 미생물 군집 수
    arr = [[0]*n for _ in range(n)]

    q = deque()
    w = deque()
    for i in range(k):
        y, x, num, d = map(int, input().split()) # y, x, 미생물수, 방향(1: 상, 2: 하, 3: 좌, 4: 우)
        arr[y][x] = [num, d]
        q.append([0, y, x, num, d])

    dy = [0,-1,1,0,0]
    dx = [0,0,0,-1,1]

    past_index = 0
    while q: # 맵에 입력
        index, y, x, num, d = q.popleft()
        if index != past_index:
            while w:    # 모여있는 군집 처리
                print(w)
                ny, nx = w.popleft()
                print(ny, nx)
                max_num = 0
                num = 0
                for a in range(len(arr[y][x])):
                    if a[0] > max_num:
                        max_num = a[0]
                        max_d = a[1]
                    num+=a[0]
                arr[y][x]=[num, max_d]

        past_index = index
        ny, nx = y+dy[d], x+dx[d]
        if ny>=n-1 or nx>=n-1 or ny<=0 or nx<=0: # 가장자리에 닿은 경우
            num//=2
            if d%2==0: 
                d-=1
            else:
                d+=1
        if arr[ny][nx]==0:
            arr[ny][nx] = [num, d]
        else:
            arr[ny][nx].append([num, d])
        if len(arr[ny][nx])>1 and [ny, nx] not in w:
            w.append([ny, nx])
        q.append([index+1, ny, nx, num, d])
        
