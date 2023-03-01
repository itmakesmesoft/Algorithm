# 3. BFS
from collections import deque
def bfs(y, x, level):
  global visited
  q = deque()
  q.append([y, x])
  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny, nx = y+dy[i], x+dx[i]
      if ny>N-1 or nx>N-1 or ny<0 or nx<0: continue
      if visited[ny][nx]==1: continue
      if MAP[ny][nx]<=level: continue # level 이하인 경우 q에 넣지 않음
      q.append([ny, nx])
      visited[ny][nx]=1 # visited에 방문처리


N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]

# 1. for문 돌려서 MAP의 모든 요소 SET로 묶기
lst = {0} # 수위를 담을 SET 생성. 비가 내리지 않는 경우는 수위가 0이므로 0 추가
for i in range(N):
  for j in range(N):
    lst.add(MAP[i][j])

# 2. SET의 요소를 하나씩 뺴서 level(수위)에 담고 while문 돌리기
max_count = 0
while lst:
  level = lst.pop() # 수위
  count = 0
  visited = [[0]*N for _ in range(N)]
  # 3. MAP을 for문 돌려 순회하면서 방문하지 않은 칸의 경우 bfs
  for i in range(N):
    for j in range(N):
      if MAP[i][j]<=level: continue # 수위보다 낮거나 같은 경우 물에 잠긴 지역이므로 스킵
      if visited[i][j]==0:
        visited[i][j]=1
        bfs(i, j, level)
        count += 1

  if count > max_count:
    max_count = count

print(max_count)







