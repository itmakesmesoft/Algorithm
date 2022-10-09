def getsum(path):
    Range = [0, path[0], path[1], n]
    word = ['W', 'B', 'R']
    cnt = 0
    for k in range(3):
        start, end = Range[k], Range[k+1]
        for i in range(start, end):
            for j in range(m):
                if lst[i][j]!=word[k]:
                    cnt+=1
    return cnt

def dfs(level, start):
    global path, min_cnt
    if level == 2:
        cnt = getsum(path)
        if cnt < min_cnt:
            min_cnt = cnt
        return
    for i in range(start+1, n):
        path[level] = i
        dfs(level+1, i)
        path[level] = 0


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    path = [0]*2
    min_cnt = 21e8
    dfs(0, 0)
    print(f'#{case} {min_cnt}')




'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW


1
4 5
WRWRW
BWRWB
WRWRW
RWBWR
'''
