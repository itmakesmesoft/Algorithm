from re import A


def Sum(arr):
    max_val = 0
    for i in range(1, m+1):
        for j in range(m-i+1): 
            tmp = sum(arr[j:i+j])
            if tmp > max_val and tmp<=c:
                max_val = tmp
                total = 0
                for k in range(j, i+j):
                    total += (arr[k]**2)
    return total      

def ispossible(level, i, j):
    global used, path
    for k in range(m):
        if used[i][j+k]==1: return False
        used[i][j+k]=1
        path[level][k]=lst[i][j+k]
    return True

def dfs(level):
    global path, used, max_total
    if level == 2:
        total = Sum(path[0]) + Sum(path[1])
        if total > max_total:
            print(path, used)
            max_total = total
        return
    for i in range(n-m+1):
        for j in range(n-m+1):
            if used[i][j]==1: continue
            backup = used[i][:]
            if ispossible(level, i, j):
                dfs(level+1)
            used[i]=backup[:]
            
            
t = int(input())
for case in range(1, t+1):
    n, m, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    used = [[0]*n for _ in range(n)]
    path = [[0]*m for _ in range(2)]
    max_total = -21e8
    dfs(0)
    print(max_total)
    
    
'''
1
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7

'''