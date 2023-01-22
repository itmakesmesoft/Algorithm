from collections import deque
def bfs(y, x):
    global visited
    level = 1
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = dy[i]+y, dx[i]+x
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if visited[ny][nx] or lst[ny][nx]==0: continue
            visited[ny][nx] = 1
            q.append([ny, nx])
            level+=1
    return level

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
max_level = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] and visited[i][j]==0:
            visited[i][j]=1
            level = bfs(i, j)
            cnt+=1
            if level > max_level:
                max_level = level
print(cnt)
print(max_level)
            