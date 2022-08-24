n = int(input())
arr = list(input().split())
def dfs(level, past, string):
    global cnt
    if level == 2:
        if string == 'HITSMUSIC':
            cnt+=1
        return
    for i in range(past, n):
        if used[i]==0:
            used[i]=1
            dfs(level+1, i, string + arr[i])
            used[i]=0
cnt = 0
used = [0]*n
dfs(0, 0, '')
print(cnt)
