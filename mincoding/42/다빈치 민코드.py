def getTotal(path):
    total = 1
    for i in range(len(path)):
        total *= path[i]
    return total
def dfs(level, start):
    global Min_path, Min, path
    if level == M:
        total = getTotal(path)
        if total < Min:
            Min = total
            Min_path = path[:] # 그냥 대입 시 주소가 할당되므로, 얕은 복사
        return
    for i in range(start, N):
        path[level]=plate[i]
        dfs(level+1, i+1)
        path[level]=0

N, M = map(int, input().split())
plate = list(map(int, input().split()))
path = [0]*M
Min_path=[]
Min = float('inf')
dfs(0, 0)
print(*sorted(Min_path))

'''
test case
7 3
1 5 4 -2 6 7 -1
'''