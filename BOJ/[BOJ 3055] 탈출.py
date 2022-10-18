from collections import deque
def bfs():
    global Map
    q = deque()
    for i in range(len(water)):            # W: 물
        q.append([water[i][0], water[i][1], 'W', 0])
    q.append([start[0], start[1], 'G', 0]) # G: 고슴도치
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    while q:
        y, x, obj, minute = q.popleft()
        if y == end[0] and x == end[1] and obj=='G':
            return minute
        
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny> r-1 or nx>c-1 or ny<0 or nx<0: continue
            if Map[ny][nx]=='X' or Map[ny][nx]=='*': continue
            if obj == 'G':
                if Map[ny][nx]=='0': continue
                Map[ny][nx]='0'
            elif obj == 'W':
                if Map[ny][nx]=='D': continue
                Map[ny][nx]='*'
            q.append([ny, nx, obj, minute+1])
    return "KAKTUS"
            
    
r, c = map(int, input().split())
Map = [list(input()) for _ in range(r)]
water = []
for i in range(r):
    for j in range(c):
        if Map[i][j]=='S':
            start = (i, j)
        elif Map[i][j]=='*':
            water.append((i, j))
        elif Map[i][j]=='D':
            end = (i, j)
print(bfs())


'''
3 3
D.*
...
.S.
'''