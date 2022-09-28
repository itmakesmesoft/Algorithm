from collections import deque
def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x= q.popleft()
        dx = [-1, 0, 1]
        for i in range(3):
            nx = x+dx[i]
            if y>5 or nx>2 or nx<0: continue
            if Map[y+1][nx]==0: continue
            tmp = lst[y][x] + Map[y+1][nx]
            if tmp > lst[y+1][nx]:
                lst[y+1][nx] = tmp
                q.append([y+1, nx])
 

Map = [list(map(int, input().split())) for _ in range(7)]
lst = [[0]*3 for _ in range(7)]
lst[0][0]=1
bfs(0,0)
print(max(lst[6]))

'''
1 0 0
1 2 2
0 3 0
3 -10 -5
15 -10 50
15 -10 10
0 6 4

'''