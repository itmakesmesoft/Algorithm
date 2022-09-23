    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue


t = int(input())
for case in range(1, t+1):
    n = int(input())
    desert = [0]*101
    visited = [[0]*n for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    desert[0]=1
    dfs(0)