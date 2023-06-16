N = int(input())
dp = [0]*(1001)
dp[1], dp[2] = 1, 2
for i in range(1,N+1):
  if i>=3:
    dp[i]=(dp[i-1]+dp[i-2])%10007
print(dp[N])