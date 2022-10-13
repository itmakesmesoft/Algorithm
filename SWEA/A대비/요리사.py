def getSum():
    global min_diff
    total = 0
    for i in range(n):
        for j in range(n):
            if path[i]==1 and path[j]==1:
                total += lst[i][j]
            elif path[i]==0 and path[j]==0:
                total -= lst[i][j]
    min_diff = min(min_diff, abs(total))
    return

def dfs(level, start):
    global path, min_diff
    if level == m:
        getSum()
        return
    for i in range(start, n):
        if path[i]==1: continue
        path[i]=1
        dfs(level+1, i+1)
        path[i]=0


t = int(input())
for case in range(1, t+1):
    n = int(input())
    m = n//2
    lst = [list(map(int, input().split())) for _ in range(n)]
    path = [0]*n
    min_diff = 21e8
    dfs(0, 0)
    print(f'#{case} {min_diff}')
    
    
    
'''
1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''