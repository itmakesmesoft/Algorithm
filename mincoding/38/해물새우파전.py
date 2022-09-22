from collections import deque

def bfs(seafood, Type):# 1 새우, 2 오징어
    q = deque()
    for i in range(len(seafood)):
        y, x = seafood[i]
        q.append([y, x, 0])
    flag = 1
    while q:
        y, x, level = q.popleft()
        if level==Type+2:
            break
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>6 or nx>6 or ny<0 or nx<0: continue
            if arr[ny][nx]==Type: flag = 0
            q.append([ny, nx, level+1])
    return flag

arr = [list(input()) for _ in range(7)]
squid = []
shrimp = []
for i in range(7):
    for j in range(7):
        if arr[i][j]=='1':
            squid.append([i, j])
        elif arr[i][j]=='2':
            shrimp.append([i, j])
if bfs(squid, 2) and bfs(shrimp, 1):
    print("pass")
else:
    print("fail")
