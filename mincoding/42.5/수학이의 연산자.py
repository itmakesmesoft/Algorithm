def methods(i, a, b):
    if i == 0:
        result = (a+b)*(a-b)
    elif i == 1:
        result = a if a>b else b
    elif i == 2:
        result = a**2 - b**2
    else:
        result = (a+b)**2
    return result

def dfs(level, total):
    global cnt
    if level == N-1:
        if total == 100:
            cnt+=1
        return

    for i in range(4):
        ret = methods(i, total, numbers[level+1])
        dfs(level+1, ret)

N = int(input())
cnt = 0
numbers = list(map(int, input().split()))
dfs(0, numbers[0]) # level, total
print(cnt)

'''
3
1 9 8
'''