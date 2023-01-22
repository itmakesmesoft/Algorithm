from collections import deque
from copy import deepcopy
import sys

def bfs():
    global lst
    tmp = deepcopy(lst)
    q = deque()
    for k in range(len(virus)):
        q.append([virus[k][0], virus[k][1]])
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
            if tmp[ny][nx]==0:
                tmp[ny][nx]=2
                q.append([ny, nx])
                
    count = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j]==0:
                count += 1
    return count

def dfs(level):
    global max_count
    if level == 3:
        # bfs로 바이러스 확산시킨 뒤 안전영역 갯수 반환
        count = bfs()
        if count > max_count:
            max_count = count
        return
    for i in range(N):
        for j in range(M):
            if lst[i][j]==0: 
                lst[i][j]=1
                dfs(level+1)
                lst[i][j]=0

def find_virus():
    global virus
    for i in range(N):
        for j in range(M):
            if lst[i][j]==2:
                virus.append((i, j))
            
            
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
max_count = 0
virus = []
find_virus()
dfs(0)
print(max_count)