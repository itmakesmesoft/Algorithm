from collections import deque

def bfs(y, x):
    global arr
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>M-1 or nx>N-1 or ny<0 or nx<0: continue
            if arr[ny][nx]>=1: continue
            arr[ny][nx]=arr[y][x]+1
            q.append([ny, nx])
    return arr[y][x]
    

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
y, x = map(int, input().split())
print(bfs(y, x))