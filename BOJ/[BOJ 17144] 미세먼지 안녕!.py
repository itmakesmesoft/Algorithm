from copy import deepcopy
def on_purifier(y, x, is_clockwise): # 공기청정기 작동 => 바람 방향대로 1칸씩 이동만 한다. 공기청정기 안으로 가면 사라짐
  global Map
  direct = [[0,1],[-1,0],[0,-1],[1,0]]
  d = prev = 0
  while True:
    ny, nx = y+direct[d][0], x+direct[d][1]
    if ny>R-1 or nx>C-1 or ny<0 or nx<0: # 방향 전환
      if is_clockwise: # 시계방향으로
        d-=1
        if d<0: d=3
      else:
        d+=1
      continue
    elif Map[ny][nx]==-1:
      break
    prev, Map[ny][nx] = Map[ny][nx], prev
    y, x = ny, nx

def spreading(): # 미세먼지 확산
  global Map
  backup = deepcopy(Map)
  direct = [[0,1],[-1,0],[0,-1],[1,0]]
  for y in range(R):
    for x in range(C):
      if backup[y][x]<=0: continue
      dust = backup[y][x]
      spread = int(dust/5)
      for i in range(4):
        ny, nx = y+direct[i][0], x+direct[i][1]
        if ny>R-1 or nx>C-1 or ny<0 or nx<0: continue
        if Map[ny][nx]==-1: continue # 공기청정기인 경우
        Map[ny][nx]+=spread
        Map[y][x]-=spread


R, C, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]
purifier = [[0, 0], [0, 0]]
for i in range(R): #공기청정기 위치 찾기
  if Map[i][0] == -1:
    purifier[0]=[i, 0]
    purifier[1]=[i+1, 0]
    break

for _ in range(T):
  spreading() # 미세먼지 확산
  on_purifier(purifier[0][0], purifier[0][1], False)
  on_purifier(purifier[1][0], purifier[1][1], True)

# 총 미세먼지량 계산
total = 0
for i in range(R):
  for j in range(C):
    if Map[i][j] == -1: continue
    total += Map[i][j]
print(total)