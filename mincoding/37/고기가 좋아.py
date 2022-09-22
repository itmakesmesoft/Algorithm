from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited = [[0]*6 for _ in range(4)]
    visited[y][x]=1
    cnt = 0
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>5 or ny<0 or nx<0: continue
            if arr[ny][nx]==1 or visited[ny][nx]==1: continue
            if arr[ny][nx]==2: cnt+=1
            visited[ny][nx]=1
            q.append([ny, nx])
    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]
print(bfs(0, 0))