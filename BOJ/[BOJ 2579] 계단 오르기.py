N = int(input())
lst = [0]+[int(input()) for _ in range(N)]

if N<=2:
    print(sum(lst))
else:
    dp = [0]*(N+3)
    for i in range(1, N+1):
        a = dp[i-2]+lst[i]
        b = dp[i-3]+lst[i-1]+lst[i]
        dp[i]=max(a, b)
    print(dp[N])