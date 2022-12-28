from collections import deque

N, M = map(int, input().split())
Map = [input() for _ in range(N)]

def find():
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 'I':
                return (i, j)
            
def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    count = 0
    while q:
        y, x = q.popleft()
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]
        if Map[y][x] == 'P':
            count += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if visited[ny][nx]==1: continue
            if Map[ny][nx] == 'X': continue
            q.append([ny, nx])
            visited[ny][nx] = 1
    return count

visited = [[0]*M for _ in range(N)]
y, x = find()
result = bfs(y, x)
if result:
    print(result)
else:
    print("TT")