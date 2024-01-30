'''
"1" 하나 선택 후 제거
=> bfs
'''

import sys, collections
input = sys.stdin.readline
d = [[0,1],[1,0],[0,-1],[-1,0]]

def is_possible(y, x):
  count = 0
  for i in range(4):
    ny, nx = y+d[i][0], x+d[i][1]
    if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
    if lst[ny][nx]=="0": count+=1
  return count>1

def bfs():
  visited = [[0]*M for _ in range(N)]
  visited[0][0] = 1
  q = collections.deque()
  q.append([0, 0, 1]) # y, x, distance

  while q:
    y, x, distance = q.popleft()
    if y==N-1 and x==M-1: return distance
    for i in range(4):
      ny, nx = y+d[i][0], x+d[i][1]
      if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
      if lst[ny][nx]=="1" or visited[ny][nx]==1: continue
      visited[ny][nx]=1
      q.append([ny, nx, distance+1])
  return -1

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
result = []
res = bfs()
if res>0: result.append(res)
for i in range(N):
  for j in range(M):
    if lst[i][j]=="1" and is_possible(i, j):
      lst[i][j]="0"
      res = bfs()
      if res>0: result.append(res)
      lst[i][j]="1"
if result==[]: print(-1)
else: print(min(result))
