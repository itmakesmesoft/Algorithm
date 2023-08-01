N = int(input())
lst = list(map(int, input().split()))
res = [0]*N

for i in range(N):
    count = 0
    for j in range(N):
        if res[j]==0:
            if count == lst[i]:
                res[j]=i+1
                break
            else:
                count+=1
print(*res)