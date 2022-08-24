def dfs(level):
    if level==n:
        for i in range(n):
            print(path[i], end='')
        print()
        return
    for i in range(len(candidates)):
        path[level]=candidates[i]
        dfs(level+1)
        path[level]=''

candidates = list(input())
n = int(input())
path = ['']*n
dfs(0)
