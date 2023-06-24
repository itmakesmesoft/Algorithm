from collections import deque

def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for i in range(N)]

    def bfs(y, x):
        nonlocal visited
        print("")
        total = 0
        q = deque()
        q.append([y, x])
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        visited[y][x]=1
        while q:
            y, x = q.popleft()
            total += int(maps[y][x])
            for i in range(4):
                ny, nx = y+direct[i][0], x+direct[i][1]
                if ny>N-1 or nx>M-1 or ny<0 or nx<0: continue
                if maps[ny][nx]=='X': continue
                if visited[ny][nx]==1: continue
                q.append([ny, nx])
                visited[ny][nx]=1
        return total

    for i in range(N):
        for j in range(M):
            if maps[i][j]!='X' and visited[i][j]==0:
                answer.append(bfs(i, j))
    if answer!=[]: answer.sort()
    else: answer.append(-1)
    return answer