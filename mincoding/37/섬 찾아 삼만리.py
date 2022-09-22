from collections import deque

def bfs(y, x):
    global visited
    visited[y][x]=1
    q=deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if Map[ny][nx]==0: continue
            visited[ny][nx]=1
            q.append([ny, nx])


N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if Map[i][j]==1 and visited[i][j]==0:
            bfs(i, j)
            cnt+=1
print(cnt)