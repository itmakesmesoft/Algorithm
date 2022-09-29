from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x= q.popleft()
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
            d = lst[ny][nx]-lst[y][x]
            if d < 0: d = 0
            if arr[y][x]+d+1 < arr[ny][nx]:
                arr[ny][nx] = arr[y][x]+d+1
                q.append([ny, nx])


t = int(input())
for case in range(1,t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    inf = int(21e8)
    arr = [[inf]*n for _ in range(n)]
    arr[0][0]=0
    bfs(0, 0)
    print(f'#{case} {arr[n-1][n-1]}')


'''
test case

3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''