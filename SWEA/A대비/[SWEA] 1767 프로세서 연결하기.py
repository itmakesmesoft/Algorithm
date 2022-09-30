from copy import deepcopy

def istherecore(y, x, dir): #True: 코어 또는 라인 있음 | False: 코어 없음
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]
    k = 1
    while True:
        ny, nx = y+dy[dir]*k, x+dx[dir]*k
        if ny>n-1 or nx>n-1 or ny<0 or nx<0: break
        elif lst[ny][nx]==1 or lst[ny][nx]==2: return True
        k+=1
    return False

def line(y, x, dir): # 코어라인 생성
    global lst
    cnt = 0
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]
    k = 1
    while True:
        ny, nx = y+dy[dir]*k, x+dx[dir]*k
        if ny>n-1 or nx>n-1 or ny<0 or nx<0: break
        lst[ny][nx]=2
        cnt +=1
        k+=1
    return cnt

def dfs(level, total, cores):
    global min_line, max_cores, lst
    if level == len(arr):
        if cores > max_cores or (cores==max_cores and min_line > total):
            min_line = total
            max_cores = cores
        return
    if min_line < total: return
    y, x = arr[level]
    backup = deepcopy(lst)
    for i in range(4):
        if istherecore(y, x, i): continue
        ret = line(y, x, i)
        dfs(level+1, total+ret, cores+1)
        lst = deepcopy(backup)
    dfs(level+1, total, cores)
    return


t = int(input())
for case in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    arr = []
    for i in range(n):
        for j in range(n):
            if lst[i][j]==1:
                arr.append([i, j])
    min_line = 21e8
    max_cores = -21e8
    dfs(0, 0, 0)
    print(f'#{case} {min_line}')


'''
test case

2
7
1 0 0 0 0 0 0
1 0 0 0 0 0 0
1 1 1 0 1 0 0
1 1 0 1 0 0 0
1 1 1 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
7
0 0 0 0 0 0 0
0 1 1 1 0 0 0
0 1 0 1 0 0 0
0 1 1 1 0 0 0
0 1 0 1 0 0 0
0 1 1 1 0 0 0
0 1 0 0 0 0 0

1
7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 1 0 1 0 0
0 1 1 1 0 0 0
0 1 1 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

1
7
0 0 0 0 0 0 0
0 1 0 1 0 1 0
0 0 1 0 1 0 0
0 1 0 0 0 1 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0


1
7
1 1 0 0 0 1 1
1 1 0 1 0 1 1
0 0 1 0 1 0 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

1
7
1 1 0 0 0 1 1
1 1 0 1 0 1 1
0 1 0 1 0 1 0
0 1 0 1 0 1 0
0 1 0 1 0 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

1
5
1 1 1 1 1
1 1 0 0 1
0 0 0 1 1
0 0 0 1 1
1 0 1 1 1
'''


