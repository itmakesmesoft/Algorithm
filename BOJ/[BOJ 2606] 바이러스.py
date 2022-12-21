def dfs(now):
    global cnt
    for i in range(N+1):
        if Map[now][i]==1 and used[i]==0:
            used[i]=1
            cnt+=1
            dfs(i)
            
N = int(input())
M = int(input())
Map = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Map[a][b] = Map[b][a] = 1
used = [0]*(N+1)
used[1]=1
cnt = 0
dfs(1)
print(cnt)
