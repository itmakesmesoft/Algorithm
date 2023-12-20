import sys
input = sys.stdin.readline

# lst의 모든 조건을 만족시키는 지 확인
def is_possible(value):
  value_set = set(value)
  for num, strike, ball in lst:
    count = [0, 0]
    num = str(num)
    for i in range(3):
      if int(num[i])==value[i]: count[0]+=1
      elif int(num[i]) in value_set: count[1]+=1
    if count[0]!=strike or count[1]!=ball: return False
  return True

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 임의의 가능한 세자리수 결정
for i in range(1, 10):
  for j in range(1, 10):
    if j==i: continue
    for k in range(1, 10):
      if k==i or k==j: continue
      if is_possible([i, j, k]):
        answer +=1
print(answer)