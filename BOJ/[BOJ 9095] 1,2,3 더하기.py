dp=[0]*11
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


T = int(input())
for i in range(T):
    N = int(input())
    print(dp[N])