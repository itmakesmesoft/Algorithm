import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
dp = [[0]*(N+1) for _ in range(N+1)]

M = int(input())
for _ in range(M):
    parent, son = map(int, input().split())
    dp[parent][son] = dp[son][parent] = 1

chon = -1
def dfs(level, me):
    global chon, visited
    if me==A:
        chon = level
        return
    for i in range(1, N+1):
        if visited[i]==0 and dp[me][i]==1:
            visited[i]=1
            dfs(level+1, i)
            visited[i]=0

visited = [0]*(N+1)
visited[B]=1
dfs(0, B)
print(chon)