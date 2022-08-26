def sumarr(y, x):
    total = 0
    for i in range(m):
        for j in range(m):
            total += arr[i+y][j+x]
    return total

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            result = sumarr(i, j)
            if result > max_sum:
                max_sum = result
    print(f'#{case} {max_sum}')