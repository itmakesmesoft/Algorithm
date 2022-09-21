from collections import deque

def bfs(st_y, st_x, ed_y, ed_x):
    q = deque()
    q.append([st_y, st_x, 0])
    visited = [[0]*M for _ in range(N)]
    visited[st_y][st_x] = 1
    while q:
        y, x, step = q.popleft()
        if y==ed_y and x==ed_x: break
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if visited[ny][nx]==1 or arr[ny][nx]=='x': continue
            visited[ny][nx]=1
            q.append([ny, nx, step+1])
    return step


N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='S':
            start_y, start_x = i, j
        elif arr[i][j]=='D':
            end_y, end_x = i, j
        elif arr[i][j]=='C':
            via_y, via_x = i, j
answer = bfs(start_y, start_x, via_y, via_x) + bfs(via_y, via_x, end_y, end_x)
print(answer)


'''
3 5
S . . D x
x . x . .
C . . . x
'''