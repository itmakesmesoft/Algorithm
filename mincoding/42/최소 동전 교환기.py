def dfs(level, total):
    global Min
    if total > rest: return
    elif total == rest:
        if level < Min:
            Min = level
        return
    for i in range(3):
        dfs(level+1, total+coins[i])

rest = int(input())
coins = [10, 40, 60]
Min = float('inf')
dfs(0, 0)
print(Min)