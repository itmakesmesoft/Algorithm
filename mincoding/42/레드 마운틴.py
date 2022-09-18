def dfs(level):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny, nx = level+dy[i], x+dx[i]
        if ny > n-1 or nx > n-1 or ny < 0 or nx < 0: continue



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
flag = 0
dfs(0, 0, 0)
if flag:
    print("가능")
else:
    print("불가능")