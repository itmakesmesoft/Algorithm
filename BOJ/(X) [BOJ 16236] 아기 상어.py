N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 현재위치 알아내기
start_y = start_x = 0
for i in range(N):
  for j in range(N):
    if lst[i][j] == 9:
      start_y, start_x = i, j

# bfs
# 상어의 크기보다 작아야함
# 현재 상어의 크기만큼 먹어야 크기+1
# 더 이상 갈 수 없는 경우 return count
from collections import deque
from copy import deepcopy
def bfs():
  global size, distance, cnt, visited, lst, start_y, start_x
  q = deque()
  q.append([start_y, start_x, 0])
  direct = [[-1, 0],[0, -1],[0, 1],[1, 0]]
  while q:
    y, x, d = q.popleft()
    for i in range(4):
      ny, nx = y+direct[i][0], x+direct[i][1]
      if ny>N-1 or nx>N-1 or ny<0 or nx<0: continue
      if visited[ny][nx]==1: continue
      if lst[ny][nx]==0 or lst[ny][nx]==size:
        q.append([ny, nx, d+1])
        visited[ny][nx] = 1
      elif lst[ny][nx]<size: # 다시 bfs
        lst[ny][nx]=0
        distance += (d+1)
        if size==cnt+1: # 크기가 커지는 경우
          size += 1
          cnt = 0
        else: # 크기가 커지지 않은 경우
          cnt += 1
        start_y, start_x = ny, nx
        return True

  return False # 더 이상 먹을게 없는 경우

size = 2
distance = 0
cnt = 0
origin_visited = [[0]*N for _ in range(N)]
while True:
  visited = deepcopy(origin_visited)
  lst[start_y][start_x]=0
  if bfs()==False:
    break
print(distance)