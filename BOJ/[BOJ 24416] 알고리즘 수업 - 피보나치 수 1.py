def fib_dp(n):
    global cnt
    memo = {1:1, 2:1}
    for i in range(3, n+1):
        cnt+=1
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

n = int(input())
cnt = 0
ret = fib_dp(n)
print(ret, cnt)