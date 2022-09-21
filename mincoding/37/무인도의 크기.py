from collections import deque

def bfs(y,x):
    visited = [[0]*4 for _ in range(4)]
    visited[y][x]=1
    q = deque()
    q.append([y, x])
    size = 0
    while q:
        y, x = q.popleft()
        size += 1
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>3 or ny<0 or nx<0: continue
            if visited[ny][nx]==0 and arr[ny][nx]==1:
                visited[ny][nx]=1
                q.append([ny, nx])
    return size
                
arr = [list(map(int, input().split())) for _ in range(4)]
print(bfs(0, 0))