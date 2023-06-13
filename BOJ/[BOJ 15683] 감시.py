# dfs로 접근
# 4회전 가능(1, 2, 3, 4번 카메라)
# 최솟값인 경우 갱신 => 반대로 많은 빈칸을 제거한 수를 구하기
from copy import deepcopy

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
lst = [] # 카메라의 좌표를 담을 리스트
K = 0 # 카메라의 갯수
max_total = 0
blank = 0

def paint(y, x, d):
    global Map
    count = 0
    direct = [[0,1],[1,0],[0,-1],[-1,0]]

    z = Map[y][x]

    if z==1:
        rng = [[0],[1],[2],[3]]
    elif z==2:
        rng = [[0,2],[1,3]]
    elif z==3:
        rng = [[0,1],[1,2],[2,3],[3,0]]
    elif z==4:
        rng = [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]
    elif z==5:
        rng = [[0,1,2,3]]

    for i in rng[d]:
        k = 1
        while True:
            ny, nx = y+direct[i][0]*k, x+direct[i][1]*k
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: break
            if Map[ny][nx]==6: break
            if Map[ny][nx]==0:
                count+=1
                Map[ny][nx]=-1
            k+=1
    return count

def dfs(depth, total):
    global Map, max_total
    backup = deepcopy(Map)
    if depth==K:
        if total>max_total:
            max_total = total
        return

    y, x = lst[depth]
    z = Map[y][x]
    if z in [1, 3, 4]: r = 4
    elif z==2: r = 2
    elif z==5: r = 1

    for d in range(r):
        tmp = paint(y, x, d)
        dfs(depth + 1, total + tmp)
        Map = deepcopy(backup)


for i in range(N):
    for j in range(M):
        if Map[i][j]==6: continue
        elif Map[i][j]!=0:
            K+=1
            lst.append([i, j])
        else:
            blank += 1

dfs(0, 0)
print(blank - max_total)