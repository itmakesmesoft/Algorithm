from collections import deque

def bfs(y1, x1, y2, x2):
    global arr
    q = deque()
    q.append([y1, x1])
    q.append([y2, x2])
    while q:
        y, x = q.popleft()
        d = [[0,1],[-1,0],[0,-1],[1,0]]
        for i in range(4):
            dy, dx = y+d[i][0], x+d[i][1]
            if dy>N-1 or dx>N-1 or dy<0 or dx<0: continue
            if arr[dy][dx] > 0: continue
            if arr[y][x]<9: arr[dy][dx]=arr[y][x]+1
            else: arr[dy][dx]=arr[y][x]
            q.append([dy,dx])
    
N= int(input())
y1, x1, y2, x2 = map(int,input().split())
arr = [[0]*N for _ in range(N)]
arr[y1][x1]=1
arr[y2][x2]=1
bfs(y1, x1, y2, x2)
for i in range(N):
    for j in range(N):
        print(arr[i][j],end='')
    print()