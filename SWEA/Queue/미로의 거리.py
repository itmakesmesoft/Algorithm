def dfs(y, x, cnt):
    global flag, result
    if arr[y][x]=='3':
        if result > cnt-1 or result == -1:
            result = cnt-1
        return
    for i in range(4):
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0 ,-1]
        ny, nx = y+dy[i], x+dx[i]
        if ny>n-1 or nx>n-1 or ny<0 or nx<0:continue
        if arr[ny][nx]!='1' and visited[ny][nx]==0:
            visited[ny][nx]=1
            dfs(ny, nx, cnt+1)
            visited[ny][nx]=0

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)] # 0: 통로, 1: 벽, 2: 출발, 3: 도착
    visited=[[0]*n for _ in range(n)]
    flag = 0
    for i in range(n):
        if flag==0:
            for j in range(n):
                if arr[i][j]=='2':
                    result = -1
                    visited[i][j]=1
                    dfs(i, j, 0)
                    if result == -1:
                        result = 0
                    print(f'#{case} {result}')
                    flag = 1
                    break



'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''