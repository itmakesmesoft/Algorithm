import sys, collections
input = sys.stdin.readline

def count_candy():
    global max_candy
    for i in range(N):
        row = 1
        col = 1
        for j in range(1, N):
            if Map[i][j] == Map[i][j-1]:
                row+=1
                if row > max_candy: max_candy = row
            else: row = 1
            if Map[j][i] == Map[j-1][i]:
                col+=1
                if col > max_candy: max_candy = col
            else: col = 1
N = int(input())
Map = [list(input()) for _ in range(N)]
max_candy = 0
d = [[0,1],[1,0],[0,-1],[-1,0]]
for y in range(N):
    for x in range(N):
        for i in range(2):
            ny, nx = y+d[i][0], x+d[i][1]
            if ny>N-1 or nx>N-1: continue
            if Map[ny][nx]!=Map[y][x]:
                Map[ny][nx], Map[y][x] = Map[y][x], Map[ny][nx]
                count_candy()
                Map[ny][nx], Map[y][x] = Map[y][x], Map[ny][nx]
print(max_candy)