import sys, collections
input = sys.stdin.readline

def bfs(tomatos):
    q = collections.deque()
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    days = 0
    for y, x in tomatos: q.append([y, x, days])

    while q:
        y, x, days = q.popleft()
        for i in range(4):
            ny, nx = y+d[i][0], x+d[i][1]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if lst[ny][nx]==0:
                lst[ny][nx]=1
                q.append([ny, nx, days+1])
    return days

def is_possible():
    for i in range(N):
        for j in range(M):
            if lst[i][j]==0: return False
    return True

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
tomatos = []
for i in range(N):
    for j in range(M):
        if lst[i][j]==1:
            tomatos.append([i, j])
days = bfs(tomatos)
if is_possible():
    print(days)
else:
    print(-1)
