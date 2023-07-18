# pypy로 제출해야 함

R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
flag = False

def dfs(y, x, dist):
    global max_dist, busket, flag

    d = [[0,1],[0,-1],[1,0],[-1,0]]
    if dist>max_dist:
        max_dist = dist
    if dist>=26 or dist>=R*C:
        flag = True
        return

    for i in range(4):
        if flag: return
        ny, nx = y+d[i][0], x+d[i][1]
        if ny>R-1 or nx>C-1 or ny<0 or nx<0: continue
        alpha = ord(Map[ny][nx])-65
        if busket[alpha]>=1: continue
        busket[alpha]=1
        dfs(ny, nx, dist+1)
        busket[alpha]=0

max_dist = 0
busket = [0]*26
busket[ord(Map[0][0])-65] = 1

dfs(0,0,1)
print(max_dist)