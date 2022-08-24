arr = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0]
]

def dfs(now):
    print(now, end=' ')
    for i in range(6):
        if arr[now][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)
visited = [0]*6
k = int(input())
visited[k]=1
dfs(k)