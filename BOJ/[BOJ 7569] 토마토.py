import sys, collections
input = sys.stdin.readline

def bfs(orders):
    q = collections.deque()
    days = 0
    for z, y, x in orders:
        q.append([x, y, z, 0]) # x, y, z, days
    d = [[0,1,0],[0,-1,0],[1,0,0],[-1,0,0],[0,0,1],[0,0,-1]]
    while q:
        x, y, z, days = q.popleft()
        for i in range(6):
            nx, ny, nz = x+d[i][0], y+d[i][1], z+d[i][2]
            if nx>M-1 or ny>N-1 or nz>H-1 or nx<0 or ny<0 or nz<0: continue
            if lst[nz][ny][nx]==0:
                lst[nz][ny][nx]=1
                q.append([nx, ny, nz, days+1])
    return days

def is_ripend():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if lst[i][j][k]==0:
                    return False
    return True

M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
orders = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k]==1:
                orders.append([i, j, k])
days = bfs(orders)
if is_ripend():
    print(days)
else:
    print(-1)
