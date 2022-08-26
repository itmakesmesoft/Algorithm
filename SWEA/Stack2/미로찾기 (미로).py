def bfs(y, x):
    global cnt, flag
    queue = [[y, x]]
    while queue:
        y, x = queue.pop(0)
        if flag==0:
            if [y, x] not in visited:
                if arr[y][x]=='3':
                    flag = 1
                    return
                cnt+=1
                visited.append([y, x])
                dy = [0,1,0,-1]
                dx = [1,0,-1,0]
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
                    if arr[ny][nx]=='1': continue
                    queue.append([ny, nx])    

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = []
    cnt = 0
    flag = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='2':
                bfs(i,j)
    if flag:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')

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