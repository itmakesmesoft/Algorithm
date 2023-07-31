import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global Map
    q = deque()
    q.append([x, y])
    Map[y][x] = 1
    area = 0

    while q:
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx, ny = x+direct[i][0], y+direct[i][1]
            if nx>N-1 or ny>M-1 or nx<0 or ny<0: continue
            if Map[ny][nx]==1: continue
            q.append([nx, ny])
            Map[ny][nx]=1
    return area

M, N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]
Map = [[0]*N for _ in range(M)] # 그림을 채울 Map 생성
direct = [[0,1],[0,-1],[1,0],[-1,0]]

while lst: # 영역 칠하기
    st_x, st_y, ed_x, ed_y = lst.pop()
    for i in range(st_y, ed_y):
        for j in range(st_x, ed_x):
            Map[i][j] = 1
res = []
for i in range(M): # 비어있는 영역 bfs 돌리기
    for j in range(N):
        if Map[i][j]==0:
            res.append(bfs(j, i))
res.sort()
print(len(res))
print(*res)