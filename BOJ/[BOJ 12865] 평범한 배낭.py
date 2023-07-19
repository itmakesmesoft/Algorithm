# Knapsack 알고리즘

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
things.sort(key=lambda x:x[0])
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        # 물건은 1개씩만 있음
        w, v = things[i-1]
        if j>=w: # 넣을 수 있는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else: # 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]
print(dp[N][K])