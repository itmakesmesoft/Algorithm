N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
result = [0]*3

def divide(y, x, step):
  global result
  if step==0:
    return Map[y][x]

  busket = [0]*9
  flag = True
  for i in range(3):
    for j in range(3):
      busket[i*3+j] = divide(y+step*i, x+step*j, step//3)

      if i==0 and j==0: continue
      elif busket[i*3+j]!=busket[i*3+j-1]:
        flag = False

  # 다른 경우 카운트
  # 같은 경우에는 카운트하지 않고 반복되는 해당 수를 반환
  if flag and busket[0]!=-2:
    return busket[0]
  else:
    for i in range(9):
      if busket[i]!=-2:
        result[busket[i]+1]+=1
    return -2
if N>=3:
  res = divide(0, 0, N//3)
  if res!=-2:
    result[res+1]+=1
else: result[Map[0][0]+1]+=1
for i in range(3):
  print(result[i])


'''
1
1

3
-1 -1 -1
-1 -1 -1
-1 -1 -1
'''