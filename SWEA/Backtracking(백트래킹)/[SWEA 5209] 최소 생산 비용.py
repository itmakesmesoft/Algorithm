def dfs(level, total):
    global min_total
    if total>min_total: return
    if level==n:
        if total<min_total:
            min_total = total
        return
    for i in range(n):
        if used[i]==1: continue
        used[i]=1
        dfs(level+1, total+lst[level][i])
        used[i]=0


t = int(input())
for case in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    used = [0]*n
    min_total = 21e8
    dfs(0, 0)
    print(f'#{case} {min_total}')
'''
test case

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4
'''