import sys
input = sys.stdin.readline

# 가로 세로 대각선 같은색 다섯개인 경우 승리
# 단, 6개 이상인 경우는 이긴 것이 아님
# 가로, 세로, +대각선, -대각선 배열 생성
plate = [list(map(int, input().split())) for _ in range(19)]
answer = [0]

# 가로 세로 검증
def garo():
  for i in range(19):
    prev = [0]*4 # [바둑색, 갯수, y좌표, x좌표]
    for j in range(19):
      cur = plate[i][j]
      print(prev)
      if cur != 0:
        if prev[0]==cur: prev[1] += 1
        elif is_answer(prev): return True
        else:
          prev[0]=cur
          prev[1]=1
      else:
        if prev[0] != 0 and prev[1]==5:
          if is_answer(prev): return True
        else:
          prev[0] = 0
          prev[1] = 0
    if is_answer(prev): return True
    return False

def sero():
  for i in range(19):
    prev = [-1,-1,-1,-1] # [바둑색, 갯수, y좌표, x좌표]
    for j in range(19):
      cur = plate[j][i]
      if cur != 0:
        if prev[0]==cur:
          prev[1] += 1
        else:
          if is_answer(prev): return True
          prev[0]=cur
          prev[1]=1
      else:
        if prev[0] != 0 and prev[1]==5:
          if is_answer(prev): return True
        else:
          prev[0] = 0
          prev[1] = 0
    if is_answer(prev): return True
    return False


'''
cur!=0
if prev==cur => prev=prev count += 1
else => prev=cur count = 1

cur==0,
if prev!=0, count==5 => 정답
else => prev = 0, count = 0

'''

def degak_leftright():
# 대각선 검증(좌상->우하)
  for i in range(19):
    prev_degak = [[-1,-1,-1,-1], [-1,-1,-1,-1]] # [바둑색, 갯수, y좌표, x좌표]
    for j in range(i, 19):
      if plate[j-i][j]==0:
        if is_answer(prev_degak[0]): return
        prev_degak[0] = [-1,-1,-1,-1]
      elif plate[j-i][j] == prev_degak[0][0]: prev_degak[0][1]+=1
      else: prev_degak[0] = [plate[j-i][j], 1, j-i, j]
      if plate[j][j-i]==0:
        if is_answer(prev_degak[1]): return
        prev_degak[1] = [-1,-1,-1,-1]
      elif plate[j][j-i] == prev_degak[1][0]: prev_degak[1][1]+=1
      else: prev_degak[1] = [plate[j][j-i], 1, j, j-i]
    is_answer(prev_degak[0]) or is_answer(prev_degak[1])


# ========================
def degak_rightleft():
  for i in range(19):
    prev_degak = [[-1,-1,-1,-1], [-1,-1,-1,-1]] # [바둑색, 갯수, y좌표, x좌표]
    for j in range(i, 19):
      if plate[j][18-j+i]==0:
        if is_answer(prev_degak[0]): return
        prev_degak[0] = [-1,-1,-1,-1]
      elif plate[j][18-j+i] == prev_degak[0][0]: prev_degak[0][1]+=1
      else: prev_degak[0] = [plate[j][18-j+i], 1, j-i, j]
      if plate[j-i][18-j]==0:
        if is_answer(prev_degak[1]):return
        prev_degak[1] = [-1,-1,-1,-1]
      elif plate[j-i][18-j]==prev_degak[1][0]: prev_degak[1][1] += 1
      else: prev_degak[1] = [plate[j-i][18-j], 1, j-i, 18-j]
    is_answer(prev_degak[0]) or is_answer(prev_degak[1])

def is_answer(param):
  global answer
  num, count, y, x = param
  num != -1 and print(param)
  if num>0 and count==5:
    answer = [num, y+1, x+1]
    return True
  return False

if garo():
  pass
# elif sero():
#   pass
# elif degak_leftright():
#   pass
# elif degak_rightleft():
#   pass

print(answer[0])
if len(answer)>1: print(*answer[1:])

'''
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
2 2 2 2 2 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 1 0 0 2 2 2 1 0 0 1 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 1 0 0 0 1 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 2 0 0 0
0 0 0 0 0 0 2 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 2 0 2 0 0 1 0 2 0 0 0 0
0 0 0 0 0 0 2 0 0 0 2 0 1 0 0 1 0 0 0
0 0 0 0 0 2 0 0 0 0 0 0 1 0 0 0 1 0 0
0 0 0 0 2 0 0 0 0 0 0 0 1 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0

'''