import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[1]+[0]*H for _ in range(N+1)]
for n in range(1, N+1):
    for h in range(1, H+1):
        dp[n][h]+=dp[n-1][h]
        for k in lst[n-1]:
            if k<=h:
                dp[n][h]+=dp[n-1][h-k]
print(dp[N][H]%10007)