def dfs(level):
    global path, Max, Min
    if level == 5:
        total = path[0]*path[1]-path[2]*path[3]+path[4]
        if total < Min:
            Min = total
        if total > Max:
            Max = total
        return
    for i in range(5):
        if used[i]==1: continue
        used[i]=1
        path[level]=lst[i]
        dfs(level+1)
        path[level]=0
        used[i]=0


lst = list(map(int, input().split()))
used = [0]*5
path = [0]*5
Max, Min = float('-inf'), float('inf')
dfs(0)
print(f'{Max}\n{Min}')