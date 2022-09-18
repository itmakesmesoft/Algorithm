def dfs(level):
    global result, Min
    backup = result
    if result == answer: 
        if Min > level:
            Min = level
        return
    if len(result)>len(answer): return
    for i in range(5):
        result += lst[i]
        dfs(level+1)
        result = backup
lst = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
Min = float('inf')
result = ''
answer = input()
dfs(0)
print(Min)
