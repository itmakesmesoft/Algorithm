from collections import deque

def bfs(y, x):
    global visited
    q = deque()
    q.append([y, x])
    visited[y][x]=1
    while q:
        y, x = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>7 or nx>8 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if arr[ny][nx]=='#':
                visited[ny][nx]=1
                q.append([ny, nx])
    return y, x

def bfs2(st_y, st_x):
    global visited
    q = deque()
    q.append([st_y, st_x, 0])
    visited[st_y][st_x]=1
    while q:
        y, x, cnt = q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>7 or nx>8 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if arr[ny][nx]=='#': 
                return cnt
            visited[ny][nx]=1
            q.append([ny, nx, cnt+1])

arr = [list(input()) for _ in range(8)]
visited = [[0]*9 for _ in range(8)]
y1, x1 = bfs(0, 8)
print(bfs2(y1, x1))


'''
______###
______###
______###
_____####
____##___
#________
##_______
###______
'''