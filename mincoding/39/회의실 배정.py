n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[1])
cnt = 1
past_end = lst[0][1]
for i in range(1, n):
    if lst[i][0] >= past_end:
        past_end = lst[i][1]
        cnt+=1
print(cnt)