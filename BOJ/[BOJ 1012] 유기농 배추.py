from collections import deque
def bfs(y, x):
    global  visited
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>n-1 or nx>m-1 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if arr[ny][nx]==0: continue
            visited[ny][nx]=1
            q.append([ny, nx])


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x]=1
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and visited[i][j]==0:
                bfs(i, j)
                cnt += 1
    print(cnt)