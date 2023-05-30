from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    # R 좌표 찾고 q에 추가 +cnt도 함께요
    used = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]\

    def find_r():
        for i in range(n):
            for j in range(m):
                if board[i][j]=='R':
                    return i, j

    def bfs():
        q = deque()
        ry, rx = find_r()
        q.append([ry, rx, 0])
        while q:
            y, x, cnt = q.popleft()
            if board[y][x] == 'G': return cnt
            direct = [[0, 1],[1, 0],[0,-1],[-1,0]]
            for i in range(4):
                j = 1
                if used[y][x][i]==1: continue
                used[y][x][i] = 1
                while True:
                    ny, nx = y+direct[i][0]*j, x+direct[i][1]*j
                    if ny>n-1 or nx>m-1 or ny<0 or nx<0 or board[ny][nx]=='D':
                        ny, nx = y+direct[i][0]*(j-1), x+direct[i][1]*(j-1)
                        q.append([ny, nx, cnt+1])
                        break
                    j+=1
        return -1

    answer = bfs()
    return answer