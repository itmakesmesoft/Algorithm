# 50분

N = int(input())
plate = [list(map(int, input().split())) for _ in range(N)]

# 메모이제이션 이용

def dfs(y, x):
  global memo
  count = 0
  cur = plate[y][x]
  if y==N-1 and x==N-1: return 1
  elif cur==0: return 0
  for i in range(2):
    ny, nx = y + cur*((i+1)%2), x + cur*((i+2)%2)
    if ny>N-1 or nx>N-1: continue
    if f'{ny}-{nx}' not in memo:
      memo[f'{ny}-{nx}'] = dfs(ny, nx)
    count += memo[f'{ny}-{nx}']
  return count

memo = {}
print(dfs(0, 0))