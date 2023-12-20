import sys
input = sys.stdin.readline
# 15분

def dfs(level, total_s, total_b):
  global used, min_diff
  if level == N:
    if sum(used) > 0: # min값 체크
      min_diff = min(min_diff, abs(total_b - total_s))
    return
  s, b = lst[level]
  used[level]=1
  dfs(level+1, total_s*s, total_b+b)
  used[level]=0
  dfs(level+1, total_s, total_b)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
min_diff = int(21e8)
used = [0]*N
dfs(0, 1, 0)
print(min_diff)