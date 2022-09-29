n = int(input())
memo = [0]*(n+1)
for i in range(1, n+1):
    if i<3:
        memo[i]=i
    else:
        memo[i]=(memo[i-1]+memo[i-2])%15746
print(memo[n])
