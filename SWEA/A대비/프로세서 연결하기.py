from copy import deepcopy

def line(y, x, dir):
    k = 0
    while True:
        k+=1
        for i in range(4):
            dy = [0,1,0,-1]
            dx = [1,0,-1,0]
            ny, nx = y+dy[i]*k, x+dx[i]*k
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: continue
            if arr[ny][nx]==1 or arr[ny][nx]==2: continue

def dfs(y, x):
    global visited
    backup = deepcopy(arr)
    for i in range(len(result)):
        if visited[i]==1: continue
        visited[i]=1
        

        visited[i]=0
    return

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            result.append([i, j])
    visited = [0]*len(result)
    y, x = result[0]
    dfs(y, x)