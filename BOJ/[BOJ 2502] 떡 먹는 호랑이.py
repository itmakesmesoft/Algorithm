D, K = map(int, input().split())
dp = [1, 1]+[0]*(D-2)

for i in range(2, D):
    dp[i]=dp[i-1]+dp[i-2]

A, B, flag = 0, 0, False

for b in range(K//dp[D-2], 0, -1):
    if flag: break
    for a in range(1, b):
        total = b*dp[D-2]+a*dp[D-3]
        if total>K: break
        elif total<K: continue
        else:
            flag = True
            A, B = a, b
            break
print(A, B, sep="\n")