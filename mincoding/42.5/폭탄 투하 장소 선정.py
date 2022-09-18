from copy import deepcopy

def victim(): #희생자수 반환
    cnt = 0
    for i in range(4):
        for j in range(4):
            if Map[i][j]=="*":
                cnt+=1
    return cnt


def explode(y, x): # 폭탄 투하지점 상하좌우에 값 변경
    global Map
    dy = [0,0,1,0,-1]
    dx = [0,1,0,-1,0]
    for i in range(5):
        ny, nx = y+dy[i], x+dx[i]
        if ny > 3 or nx > 3 or ny < 0 or nx < 0: continue
        if Map[ny][nx]!="_":
            Map[ny][nx]="*"
    return

def dfs(level, y, x):
    global Max, Max_path, Map, path
    backup = deepcopy(Map)
    if level == N:
        total = victim()
        if Max < total:
            Max = total
            Max_path = deepcopy(path)
        return
    for i in range(4):
        for j in range(4):
            if (i<=y+2 and i>=y-2) and (j<=x+2 and j>=x-2): continue
            if (i<=y+1 and i>=y-1) and (j<=x+1 and j>=x-1): continue
            explode(i, j)
            path[level]=[i, j]
            dfs(level+1, i, j)
            path[level]=[]
            Map = deepcopy(backup)

Map = [list(input()) for _ in range(4)]
N = int(input())
Max = -21e8
Max_path = []
result = []
path = [[0,0] for _ in range(N)]
dfs(0, 0, 0)
for i in range(N):
    y,x = Max_path[i]
    result.append(Map[y][x])
result.sort()
print(*result)
