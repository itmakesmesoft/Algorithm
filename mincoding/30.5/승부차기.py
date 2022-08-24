def dfs(now, res):
    if now==n:
        for i in range(n):
            print(res[i], end='')
        print()
        return
    for i in range(2):
        dfs(now+1, res+[arr[i]])

arr = ['o', 'x']
n = int(input())
dfs(0, [])