from copy import deepcopy
def rotate():
  tmp = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      tmp[i][j] = Map[j][N-i-1]
  return tmp

def is_possible(row, index, reverse):
  global used
  if reverse:
    start, end, step = index+L, index-1, -1
  else:
    start, end, step = index-L, index+1, 1
  if start<0 or start > N-1 or end<-1 or end>N: return False # 범위를 벗어나는 경우 false

  prev_value = Map[row][start]
  for i in range(start, end, step):
    if i==index and abs(Map[row][i]-prev_value) == 1:
      return True
    elif abs(Map[row][i]-prev_value) >1:
      return False
    elif used[row][i]==0:
      used[row][i]=1
    else:
      return False
  return True


N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
count = 0

for k in range(2):
  used = [[0]*N for _ in range(N)]
  for i in range(N):
    prev = Map[i][0]
    flag = True
    for j in range(N):
      if Map[i][j] != prev:
        if Map[i][j]-prev > 0: # 높아질 때 검증
          if is_possible(i, j, False)==False:
            flag = False
        elif Map[i][j]-prev < 0: # 낮아질 때 검증
          if is_possible(i, j-1, True)==False:
            flag = False
        prev = Map[i][j]
      # 높낮이 변화 없으면 통과
    if flag: count+=1
  if k==0:
    Map = deepcopy(rotate())
print(count)

'''
2 1
3 2
1 0
'''