from collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    cnt = 1
    def bfs(y, x):
        nonlocal cnt, visited
        q = deque()
        q.append([y, x, cnt])
        direct = [[1, 0],[0 ,1],[-1, 0],[0, -1]]
        while q:
            y, x, cnt = q.popleft()
            if y==n-1 and x==m-1:
                return cnt
            for i in range(4):
                ny, nx = y+direct[i][0], x+direct[i][1]
                if ny>n-1 or nx>m-1 or ny<0 or nx<0: continue
                if visited[ny][nx]==1: continue
                if maps[ny][nx]==0: continue
                visited[ny][nx]=1
                q.append([ny, nx, cnt+1])
        return -1
    answer = bfs(0, 0)
    return answer