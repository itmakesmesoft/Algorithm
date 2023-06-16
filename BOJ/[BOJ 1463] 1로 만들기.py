# 3으로 나누어 떨어지는 경우
# 2로 나누어 떨어지는 경우
# 1을 빼는 경우

N = int(input())
dp = [0]*(1000001)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(1, N+1):
    if i<=4: continue
    # 6의 배수인 경우
    if i%2==0 and i%3==0:
        dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1
    # 2의 배수인 경우
    if i%2==0:
        dp[i] = min(dp[i//2], dp[i-1])+1
    # 3의 배수인 경우
    elif i%3==0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    # 2 또는 3의 배수가 아닌 경우
    else:
        dp[i] = dp[i-1]+1
print(dp[N])

