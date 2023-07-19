# Google 참고

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()

dp = [0]*(K+1)
dp[0] = 1 # 가치가 0일때의 경우의 수 초기화

for coin in coins:
    for i in range(coin, K+1):
        dp[i]+=dp[i-coin]

print(dp[K])