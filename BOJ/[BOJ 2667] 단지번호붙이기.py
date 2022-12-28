N = int(input())
Map = [input() for _ in range(N)]

from collections import deque
def bfs(y, x):
    count = 0
    global visited
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        count+=1
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>N-1 or ny<0 or nx<0: continue
            if Map[ny][nx]=='1' and visited[ny][nx]==0:
                visited[ny][nx] = 1
                q.append([ny, nx])
    return count

visited = [[0]*N for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if Map[i][j]=='1' and visited[i][j]==0:
            visited[i][j] = 1
            result.append(bfs(i, j))
            cnt += 1
print(cnt)
result.sort()
for i in result:
    print(i)
    
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''