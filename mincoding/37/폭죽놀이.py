from collections import deque

def bfs(lst):
    q = deque()
    for i in range(len(lst)):
        q.append([lst[i][0], lst[i][1], 0])
    while q:
        y, x, cnt = q.popleft()
        dy = [0,1,1,1,0,-1,-1,-1]
        dx = [1,1,0,-1,-1,-1,0,1]
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx > 4 or ny<0 or nx<0: continue
            if arr[ny][nx]>0: continue
            arr[ny][nx]=1
            q.append([ny, nx, cnt+1])
    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]
lst = []
for i in range(4):
    for j in range(5):
        if arr[i][j]==1:
            lst.append([i, j, 0])
print(bfs(lst))