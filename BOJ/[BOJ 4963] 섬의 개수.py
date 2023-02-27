import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    q = deque()
    q.append([y, x])
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if ny>h-1 or nx>w-1 or ny<0 or nx<0: continue
            if visited[ny][nx] == 1: continue
            if MAP[ny][nx]==1:
                visited[ny][nx]=1
                q.append([ny, nx])


while True:
    w, h = map(int, input().split())
    if w == h == 0: break
    MAP = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                bfs(i, j)
                count+=1
    print(count)