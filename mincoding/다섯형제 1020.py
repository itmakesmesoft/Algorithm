arr = list(map(int, input().split()))

def dfs(level, total):
    global cnt
    if total >= 10 and total <= 20:
        cnt+=1
        return
    elif level == 5:
        return
    
    dfs(level+1, total+arr[level])
    dfs(level+1, total)
cnt = 0
dfs(0, 0)
print(cnt)