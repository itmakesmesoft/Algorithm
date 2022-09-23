'''
test case
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''

def dfs(level, index, total):
    global min_total
    if total>min_total: return
    if level==n-1:
        a_total = total+arr[index][0]
        if a_total < min_total:
            min_total = a_total
        return
    for i in range(1, n):
        if visited[i]==1: continue
        if index == i: continue
        visited[i]=1
        dfs(level+1, i, total+arr[index][i])
        visited[i]=0


t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    min_total = 21e8
    dfs(0, 0, 0)
    print(f'#{case} {min_total}')


