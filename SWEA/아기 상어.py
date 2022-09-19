from collections import deque

def bfs(y, x):
    global cntTable, area
    sec = 0
    cnt = 0
    me=2
    q = deque()
    q.append([y, x])
    while q:
        if cntTable[max_val]==0: break
        if cnt==me:
            me += 1
            cnt = 0
        now = q.popleft()
        y, x = now
        if area[y][x] < me and area[y][x]>0: 
            print(y, x)
            cnt+=1
            area[y][x]=0
            cntTable[area[y][x]]-=1   
        dy = [0,1,0,-1]
        dx = [-1,0,1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>N-1 or ny<0 or nx<0: continue
            q.append([ny,nx])
            sec+=1
    return sec

N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
cntTable = [0]*7
for i in range(N):
    for j in range(N):
        val = area[i][j]
        if val == 9:
            start=(i, j)
        elif val > 0:
            cntTable[val]+=1
max_val = 0
me = 2
for i in range(1,7):
    if cntTable[i]>=me-1:
        max_val = i
        me+=1
print(bfs(start[0], start[1]))