from copy import deepcopy

def rotate(r, c, s):
    # 중심(r, c)을 기준으로 1, 2, ... s-1, s까지 범위 확대하며 회전
    # s=1일때, 2칸씩 4번 회전, s=2일때, 4칸씩 4번 회전, s=3일때, 6칸씩 4번 회전 ...
    for i in range(1, s+1):
        d = [[0,-1],[-1,0],[0,1],[1,0]]
        tmp = Map[r+i][c+i]
        y, x = r+i, c+i
        for j in range(4):
            for _ in range(1, i*2+1):
                y, x = y + d[j][0], x + d[j][1]
                Map[y][x], tmp = tmp, Map[y][x]
             
                
def get_sum(Map):
    min_t = int(21e8)
    for m in Map:
        t = sum(m)
        if t < min_t:
            min_t = t
    return min_t


def dfs(level):
    global Map, min_total
    if level == ln:
        total = get_sum(Map)
        if total < min_total:
            min_total = total
        return
    copied = deepcopy(Map)
    for i in range(ln):
        if used[i]: continue
        used[i] = 1
        r, c, s = orders[i]
        rotate(r-1, c-1, s)
        dfs(level+1)
        Map = deepcopy(copied)
        used[i] = 0
   
        
N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(K)]
min_total = int(21e8)
ln = len(orders)
used = [0]*ln

dfs(0)
print(min_total)
