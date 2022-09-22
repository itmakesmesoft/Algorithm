from collections import deque

def bfs(y, x, val):
    global visited
    q = deque()
    q.append([y, x])
    cnt = 1
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>8 or ny<0 or nx<0: continue
            if arr[ny][nx]!=val: continue
            if visited[ny][nx]==1: continue
            cnt+=1
            visited[ny][nx]=1
            q.append([ny, nx])
    return cnt


arr = [list(map(int,input().split())) for _ in range(4)]
visited = [[0]*9 for _ in range(4)]
max_cnt = max_val = 0
for i in range(4):
    for j in range(9):
        if visited[i][j]==0:
            visited[i][j]=1
            val = arr[i][j]
            cnt = bfs(i, j, val)
            if max_cnt<cnt:
                max_cnt=cnt
                max_val=val
print(max_val*max_cnt)
