# 문제 1.
'''
t = int(input())
for case in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    res = [[0]*2*n for _ in range(2*n)] # 결과를 저장할 리스트 생성
    for i in range(2*n):
        for j in range(2*n):
            if i<n and  j>=n:   # 1사분면
                res[i][j]=lst[i][2*n-1-j]
            elif i<n and j<n:   # 2사분면
                res[i][j]=lst[i][j]
            elif i>=n and j<n:  # 3사분면
                res[i][j]=lst[2*n-1-i][j]
            else:               # 4사분면
                res[i][j]=lst[2*n-1-j][2*n-1-i]

    print(f'#{case}')           # 출력
    for i in range(len(res)):
        print(*res[i])
'''


# 문제 2.
'''
def dfs(level, total):
    global used, min_total
    if total>min_total: return
    if level==n:
        if total<min_total:
            min_total = total
        return
    for i in range(n):
        if used[i]==1: continue
        used[i]=1
        dfs(level+1, total+arr[level][i])
        used[i]=0

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0]*n
    min_total = 21e8
    dfs(0, 0)
    print(f'#{case} {min_total}')
'''


# 문제 3.
'''
def dfs(level, total, e_y, e_x):
    global used, min_total
    if total>min_total: return
    if level==n:
        if total<min_total:
            min_total = total
        return
    if level == e_y:
        dfs(level+1, total, e_y, e_x)
        return
    for i in range(n):
        if used[i]==1: continue
        if i==e_x: continue
        used[i]=1
        dfs(level+1, total+arr[level][i], e_y, e_x)
        used[i]=0

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0]*n
    min_total = 21e8
    for i in range(n):
        for j in range(n):
            dfs(0, 0, i, j)
    print(f'#{case} {min_total}')
'''