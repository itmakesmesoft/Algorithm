import sys, collections;
input = sys.stdin.readline

def bfs(y, x):
  q = collections.deque()
  q.append([y, x, 0]) # [y, x, distance]
  d = [[-1,0],[1,0],[0,-1],[0,1]]
  answer = [[0]*M for _ in range(N)]
  visited = [[0]*M for _ in range(N)]
  visited[y][x] = 1

  while q:
    y, x, distance = q.popleft()
    answer[y][x]=distance
    for i in range(4):
      ny, nx = y+d[i][0], x+d[i][1]
      if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
      if lst[ny][nx]==0 or visited[ny][nx]==1: continue
      visited[ny][nx]=1
      q.append([ny, nx, distance+1])
  return answer

def find_destination():
  for i in range(N):
    for j in range(M):
      if lst[i][j]==2:
        return [i, j]
  return [-1, -1]


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
y, x = find_destination()

answer = bfs(y, x)
for i in range(N):
  for j in range(M):
    if answer[i][j]==0 and lst[i][j]==1:
      answer[i][j]=-1

for i in range(N):
  print(*answer[i])
