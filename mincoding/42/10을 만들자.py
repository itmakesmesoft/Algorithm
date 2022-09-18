def dfs(level, total):
    global cnt
    if total > 10: return
    if level == N:
        if total == 10:
            cnt+=1
        return
    for i in range(1, 10):
        dfs(level+1, total+i)
N = int(input())
cnt = 0
dfs(0, 0)
print(cnt)