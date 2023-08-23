import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*501 for _ in range(501)]
for _ in range(N):
    a, b = map(int, input().split())
    dp[a][b]=1

for i in range(1, 501):
    for j in range(1, 501):
        if dp[i][j]==1:
            dp[i][j]=dp[i-1][j-1]+1
        elif dp[i-1][j]>0 or dp[i][j-1]>0:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(N-dp[500][500])