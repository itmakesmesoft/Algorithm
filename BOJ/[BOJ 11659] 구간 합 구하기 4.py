import sys
input = sys.stdin.readline


n, m = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(1, n):
    lst[i]+=lst[i-1]
result = [0]*m
for j in range(m):
    l, r = map(int, input().split())
    if l>1:
        result[j] = lst[r-1]-lst[l-2]
    else:
        result[j] = lst[r-1]
for k in range(m):
    print(result[k])