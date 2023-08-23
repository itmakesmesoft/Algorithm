import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# LIS 알고리즘 기본문제
dp = [[1]*(N) for _ in range(2)]
answer = [0]*N
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]: # 증가하는 수열 찾기
            dp[0][i] = max(dp[0][j]+1, dp[0][i])

        if A[N-i-1] > A[N-j-1]:
            dp[1][N-i-1] = max(dp[1][N-j-1]+1, dp[1][N-i-1])

for i in range(N):
    answer[i]=dp[0][i]+dp[1][i]-1
print(max(answer))