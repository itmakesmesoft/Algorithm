a = input()
b = input()

n, m = len(a), len(b)
print(n, m)
lst = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, m+1):
    if a[i-1]==b[j-1]:
      lst[i][j] = lst[i-1][j-1]+1
    else:
      lst[i][j] = max(lst[i][j-1], lst[i-1][j])
print(lst[n][m])