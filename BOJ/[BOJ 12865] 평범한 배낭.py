N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

def dfs(level, w, v):
  global used, max_v
  if w > K:
    return
  else:
    if v > max_v:
      max_v = v
  for i in range(N):
    if used[i]==1: continue
    used[i]=1
    dfs(level+1, w+lst[i][0], v+lst[i][1])
    used[i]=0
  return

max_v = 0
used = [0]*N
dfs(0, 0, 0)
print(max_v)