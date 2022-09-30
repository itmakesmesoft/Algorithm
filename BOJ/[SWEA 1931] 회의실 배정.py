n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:(x[1], x[0]))
cnt = 1
past_end = lst[0][1]
for i in range(1, n):
    start, end = lst[i]
    if start>=past_end:
        cnt+=1
        past_end = end
print(cnt)

'''
2
1 1
0 1

2
0 1
1 1
'''