# 별 동그라미 네모 세모 = 4 3 2 1
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    bucket_a = [0]*5
    bucket_b = [0]*5
    for i in range(1, a[0]+1):
        bucket_a[a[i]]+=1
    for i in range(1, b[0]+1):
        bucket_b[b[i]]+=1

    j = 4
    winner = 'D'
    while j > 0:
        if bucket_a[j]>bucket_b[j]:
            winner = 'A'
            break
        elif bucket_a[j]<bucket_b[j]:
            winner = 'B'
            break
        j -= 1
    print(winner)