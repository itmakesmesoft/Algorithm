arr = list(map(int, input().split()))

def dfs(level, total, pastidx):
    global cnt
    if total>20:
        return
    if total >= 10:
        cnt+=1
    for i in range(pastidx, 5):
        if used[i]==0:
            used[i]=1
            dfs(level+1, total + arr[i], i)
            used[i]=0
used = [0]*5
cnt = 0
dfs(0, 0, 0)
print(cnt)