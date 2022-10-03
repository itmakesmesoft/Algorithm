def combo(n, r):
    res = 1
    for i in range(n-r+1, n+1):
        res*=i
    for i in range(1, r+1):
        res//=i
    return res

t = int(input())
for case in range(1, t+1):
    r, n = map(int, input().split())
    result = combo(n, r)
    print(result)