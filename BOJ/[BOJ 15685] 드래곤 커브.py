# 1x1 정사각형의 갯수 구하기
def count_rectangle():
  direct = [[0,0],[0,1],[1,0],[1,1]]
  count = 0
  for i in range(100):
    for j in range(100):
      for k in range(4):
        y, x = i+direct[k][0], j+direct[k][1]
        if Map[y][x]==0:
          break
      else:
        count+=1
  return count

# g 만큼 2^g 번 루프(방향)을 돎
def curve(x, y, d, g):
  global Map
  direct = [[1, 0],[0, -1],[-1, 0],[0, 1]]
  # 0: x 증가
  # 1: y 감소
  # 2: x 감소
  # 3: y 증가
  lst = [d]

  Map[y][x] = 1
  y, x= y+direct[d][1], x+direct[d][0]
  Map[y][x] = 1

  for i in range(g):
    tmp = []
    for j in range(len(lst)-1, -1, -1):
      t = (lst[j]+1)%4
      ny, nx = y+direct[t][1], x+direct[t][0]
      Map[ny][nx] = 1
      y, x = ny, nx
      tmp.append(t)
    lst = lst+tmp[:]
  return Map

N = int(input())
Map = [[0]*101 for _ in range(101)]
for _ in range(N):
  x, y, d, g = map(int, input().split())
  curve(x, y, d, g)
print(count_rectangle())