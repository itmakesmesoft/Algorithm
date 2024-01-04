# 120분
N = int(input())
lst = list(map(int, input().split()))
res = lst[:]

for i in range(N):
  for j in range(i):
    if lst[j]<lst[i] and res[i]<res[j]+lst[i]:
      res[i] = res[j]+lst[i]
print(max(res))