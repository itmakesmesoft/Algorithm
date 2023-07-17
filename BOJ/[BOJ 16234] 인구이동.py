# while문 돌며 인구이동 발생하는 지 체크
# 인구 이동 발생 조건이면 bfs
# 딕셔너리 이용 -> lst[][]>100이면 딕셔너리 값 체크
# bfs는 이전값을 가지고 있어야함
# visited 사용

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
popularity = dict()
k = 101

def bfs(r, c):
    global visitied, k
    q = deque()
    q.append([r, c, lst[r][c]])
    visitied[r][c]=1
    total = 0
    count = 0

    while q:
        r, c, cur = q.popleft()
        if cur>100: cur= popularity[cur]
        lst[r][c] = k # 해당 칸의 값을 딕셔너리 값으로 대체
        total += cur
        count += 1
        d = [[0, 1],[0,-1],[1,0],[-1,0]]
        for i in range(4):
            nr, nc = r+d[i][0], c+d[i][1]
            if nr>N-1 or nc>N-1 or nr<0 or nc<0: continue
            if visitied[nr][nc]==1: continue
            if lst[nr][nc]>100: # 딕셔너리 값 이용해야함
                nxt = popularity[lst[nr][nc]]
            else:
                nxt = lst[nr][nc]
            diff = abs(cur-nxt)
            if diff<L or diff>R: continue
            q.append([nr, nc, nxt])
            visitied[nr][nc]=1
    popularity[k] = int(total/count)
    k += 1
    return count

flag = True
days = -1
while flag:
    flag = False
    days+=1
    visitied = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visitied[i][j]==1: continue
            if bfs(i, j)>1: flag = True

print(days)