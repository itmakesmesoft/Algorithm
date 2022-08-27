n = int(input())
line = list(map(int, input().split()))
result = list(range(1, n+1))
for i in range(1, n):
    k = line[i] # 앞으로 이동해야 할 칸 수
    for j in range(i, i-k, -1):
        result[j], result[j-1] = result[j-1], result[j]
print(*result)