import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(N+2) for _ in range(2)]
    for j in range(N):
        for i in range(2):
            if j>0:
                a = dp[(i+1)%2][j-2] + stickers[i][j]
                b = dp[(i+1)%2][j-1] + stickers[i][j]
                dp[i][j] = max(a, b)
            else:
                dp[i][j] = stickers[i][j]
    print(max(dp[0][N-1], dp[1][N-1]))
