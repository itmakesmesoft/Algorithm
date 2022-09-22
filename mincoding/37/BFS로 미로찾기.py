from collections import deque

def bfs(st_y, st_x, ed_y, ed_x):
    q = deque()
    q.append([st_y, st_x, 0])
    visited = [[0]*4 for _ in range(4)]
    visited[st_y][st_x] = 1
    while q:
        y, x, steps = q.popleft()
        if y==ed_y and x==ed_x: break
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>3 or ny<0 or nx<0: continue
            if arr[ny][nx]==1: continue
            if visited[ny][nx]==1: continue
            visited[ny][nx]=1
            q.append([ny, nx, steps+1])
    return steps

arr = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0]
]
start_y, start_x = map(int, input().split())
end_y, end_x = map(int, input().split())
steps = bfs(start_y, start_x, end_y, end_x)
print(f'{steps}회')