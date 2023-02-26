def count_eggs():
  global max_cnt
  count = 0
  for i in range(N):
    if lst[i][0]<=0:
      count+=1
  if count > max_cnt:
    max_cnt = count

def dfs(level):
  global lst
  if level==N:
    count_eggs()
    return

  if lst[level][0]<=0: #내가 손에 든 계란이 이미 깨져있는 경우
    dfs(level+1)
    return

  for i in range(N):
    if i==level:
      count_eggs()
      continue # 바로 이전과 같은 계란은 스킵하기
    if lst[i][0]<=0: continue # 이미 깨진 계란
    # 내구도 백업
    tmp_a, tmp_b = lst[level][0], lst[i][0]
    # 다음 내구도 = 내구도-무게
    lst[level][0], lst[i][0] = lst[level][0]-lst[i][1], lst[i][0]-lst[level][1]
    dfs(level+1)
    lst[level][0], lst[i][0] = tmp_a, tmp_b # 되돌리기


import sys
input = sys.stdin.readline

N = int(input())
max_cnt = 0
lst = []

for _ in range(N):
  a, b = map(int, input().split()) # 0:내구도, 1:무게
  lst.append([a, b])
dfs(0)
print(max_cnt)