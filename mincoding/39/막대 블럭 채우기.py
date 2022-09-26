def dfs(total, cnt):
    global max_cnt
    if total>100: return
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(n):
        if used[i]==0:
            used[i]=1
            dfs(total + lst[i], cnt+1)
            used[i]=0

n = int(input())
lst = list(map(int, input().split()))
used = [0]*n
max_cnt = -21e8
dfs(0, 0)
print(max_cnt)

'''
test case

6
20 57 13 40 33 8
'''