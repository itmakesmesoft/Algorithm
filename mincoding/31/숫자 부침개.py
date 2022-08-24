p = int(input())
n = int(input())
for _ in range(n):
    p *= 2
    res = 0
    while p>0:
        res *= 10
        res += p%10 # 나머지
        p//=10 # 다음
    p = res
print(p)




