import sys, collections
input = sys.stdin.readline

R, C, N = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]

for i in range(R):
  for j in range(C):
    if lst[i][j] == ".":
      lst[i][j] = 0
    else:
      lst[i][j] = 3
q = collections.deque()

for k in range(N):
  for i in range(R):
    for j in range(C):
      if lst[i][j] == 1:
        q.append([i, j])
      elif (k > 1 and lst[i][j]==0) or lst[i][j] == -1:
        lst[i][j] = 3
      else:
        lst[i][j] -= 1
  while q:
    y, x = q.popleft()
    d = [[0,0], [0,1],[0,-1],[1,0],[-1,0]]
    for i in range(5):
      ny, nx = y+d[i][0], x+d[i][1]
      if ny > R-1 or nx > C-1 or ny < 0 or nx < 0: continue
      if lst[ny][nx] == 0: continue
      lst[ny][nx] = 0

for i in range(R):
  for j in range(C):
    if lst[i][j] < 1:
      lst[i][j] = "."
    else:
      lst[i][j] = "O"

for i in range(R):
  print(*lst[i], sep="")