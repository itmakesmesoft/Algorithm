def rotate(index):
    global cube
    for i in range(len(cube)-1, 0, -1):
        cube[index][i], cube[index][i-1] = cube[index][i-1], cube[index][i]

def getTotal(cube):
    total = 1
    for i in range(len(cube)):
        col_total = 0
        for j in range(len(cube)):
            col_total+=cube[j][i]
        total *= col_total
    return total

def dfs(level):
    global cube, Max
    if level == n:
        total = getTotal(cube)
        if total > Max:
            Max = total
        return

    for i in range(n-1):
        dfs(level+1)
        rotate(level)

n = int(input())
cube = [list(map(int,input().split())) for _ in range(n)]
Max = float('-inf')
dfs(0)
print(f'{Max}점')