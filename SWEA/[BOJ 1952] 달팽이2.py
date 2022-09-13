m, n = map(int, input().split())
cnt = 0
while n>0 and m>0:
    if m >= 3 and n >= 3:
        cnt += 4
    elif m >= 3 and n == 2:
        cnt += 3
    elif m == 2 and n>=2:
        cnt += 2
    elif m>1 and n==1:
        cnt += 1
    n-=2
    m-=2
print(cnt)