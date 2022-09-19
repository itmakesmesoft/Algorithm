def dfs(y, x):
    global arr, flag
    if flag:
        return
    if y==n-1 and x==n-1:
        flag = 1
        return
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny > n-1 or nx > n-1 or ny < 0 or nx < 0: continue
        if arr[ny][nx]==1 or arr[ny][nx]==2: continue
        arr[y][x]=2
        dfs(ny, nx)
        arr[y][x]=0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
flag = 0
dfs(0, 0)
if flag:
    print("가능")
else:
    print("불가능")

'''
3
0 1 0
0 1 1
0 0 0


5
0 1 0 0 0
0 1 1 1 0
0 0 0 1 0
1 1 0 1 0
0 0 0 1 0
'''