lst = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(4):
        if j>0 and i==0:
            lst[i][j]+=lst[i][j-1]
        elif i>0 and j==0:
            lst[i][j]+=lst[i-1][j]
        else:
            if i>0 and j>0:
                if lst[i-1][j]>lst[i][j-1]: # 위
                    lst[i][j]+=lst[i][j-1]
                else: # 왼쪽
                    lst[i][j]+=lst[i-1][j]

from collections import deque
def bfs(y, x):
    q = deque()
    q.append([y, x])
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    result = [[y, x]]
    while q:
        # print(result)
        y, x = q.popleft()
        min_val = lst[y][x]
        min_y, min_x = y, x
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny>3 or nx>3 or ny<0 or nx<0: continue
            if lst[ny][nx] <= min_val:
                min_val = lst[ny][nx]
                min_y, min_x = ny, nx
        result.append([min_y, min_x])
        if min_y == 0 and min_x == 0: break
        q.append([min_y, min_x])
    return result

ret = bfs(3, 3)
for i in range(len(ret)-1, -1, -1):
    print(f'{ret[i][0]},{ret[i][1]}')

'''
test case
0 3 5 1
1 1 1 5
1 50 20 10
1 50 5 0
'''