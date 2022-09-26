from collections import deque

def bfs(y, x, number):
    q = deque()
    q.append([y, x, 0])
    visited = [[0]*M for _ in range(N)]
    visited[y][x]=1

    while q:
        y, x, cnt = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        if Map[y][x]!='0':
            if int(Map[y][x])==number:
                break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if Map[ny][nx]=='#': continue
            visited[ny][nx]=1
            q.append([ny, nx, cnt+1])
    return y, x, cnt

N, M = map(int,input().split())
Map = [list(input()) for _ in range(N)]

y = x = 0
total = 0
for num in range(1, 5):
    y, x, cnt = bfs(y, x, num)
    total += cnt
print(f'{total}회')

