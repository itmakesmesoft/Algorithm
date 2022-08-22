def dsum(y,x):
    d=[[0,1],[1,0],[0,-1],[-1,0]]
    total = 0
    for i in range(4):
        dy = y + d[i][0]
        dx = x + d[i][1]
        if dy>n-1 or dx > n-1 or dy < 0 or dx < 0:continue
        value = arr[y][x]- arr[dy][dx]
        if value < 0:
            value*=(-1)
        total += value
    return total



for case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            total += dsum(i, j)
    print(f'#{case} {total}')