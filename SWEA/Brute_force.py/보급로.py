from collections import deque

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    lst = [[21e8]*n for _ in range(n)]
    lst[0][0] = 0
    q = deque()
    q.append([0,0])
    while q:
        y, x = q.popleft()
        if y == n-1 and x == n-1: break
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
            tmp = lst[y][x] + int(arr[ny][nx])
            if tmp < lst[ny][nx]:
                lst[ny][nx] = tmp
                q.append([ny, nx])

    print(f'#{case} {lst[n-1][n-1]}')
