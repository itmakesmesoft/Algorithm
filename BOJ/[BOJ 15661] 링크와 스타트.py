# 30분

import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
# 스타트팀을 기준으로 1 ~ N-1명까지 뽑는 경우 구하기 => 조합

used = [0]*N
def dfs(start, count):
  global used, min_diff
  if count == total: # 여기서 합계 구해야 함
    # print(used)
    min_diff = min(min_diff, get_diff())
    return
  if start > N-1: return
  for i in range(start, N):
    if used[i]==1: continue
    used[i]=1
    dfs(i+1, count+1)
    used[i]=0

def get_diff(): # 나눠진 팀의 점수 차 구하기
  total_a = total_b = 0
  for i in range(N):
    for j in range(N):
      if i==j or used[i]!=used[j]: continue
      if used[j]==1: # 스타트 팀(a)인 경우
        total_a += S[i][j]
      else:          # 링크 팀(b)인 경우
        total_b += S[i][j]
  return abs(total_a - total_b)

min_diff = int(21e8)
for total in range(1, N):
  dfs(0, 0)
print(min_diff)

'''
20
0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 24 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


'''