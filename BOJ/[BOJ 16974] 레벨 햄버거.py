# 경우의 수
# B BPPPB P BPPPB B
# 1. X == 1
# 2. X가 가운데 P 이전
# 3. X가 가운데 P
# 4. X가 가운데 P와 마지막 B 사이
# 5. X가 마지막 B


def recur(x, n):
    if n == 0:
        return x
    if x==1:
        return 0
    elif x <= 1+layer[n-1]:
        return recur(x-1, n-1)
    elif x == 2+layer[n-1]:
        return patty[n-1] + 1
    elif x <= 2+2*layer[n-1]:
        return patty[n-1] + 1 + recur(x-layer[n-1]-2, n-1)
    else:
        return patty[n]


N, X = map(int, input().split())

layer = [1]*51
patty = [1]*51

for i in range(1, N+1):
    layer[i] = 2*layer[i-1] + 3
    patty[i] = 2*patty[i-1] + 1

print(recur(X, N))

