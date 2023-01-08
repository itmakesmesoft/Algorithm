def dfs(row):
    global status, visited
    if status == "CYCLE": return
    if row == N: return
    
    for i in range(1, N+1):
        if Map[row][i] == 1:
            if visited[i]==1: 
                status = "CYCLE"
                return
            visited[i]=1
            dfs(i)
            visited[i]=0


N = int(input())
visited = [0]*(N+1)
Map = [[0]*(N+1) for _ in range(N+1)]
status = "NO CYCLE"

for i in range(1, N):
    M = int(input())
    lst = list(map(int, input().split()))
    for j in lst:
        Map[i][j] = 1

dfs(1)
print(status)