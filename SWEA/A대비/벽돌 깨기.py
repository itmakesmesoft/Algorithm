from collections import deque
from copy import deepcopy

def drop_bricks():
    global lst, cnt_brick
    for j in range(0, w):
        tmp = []
        for i in range(h-1, -1, -1):
            if lst[i][j]==0:
                tmp.append(i)
            elif tmp:
                t_y = tmp.pop(0)
                tmp.append(i)
                lst[t_y][j], lst[i][j] = lst[i][j], lst[t_y][j]
        cnt_brick[j]=h-tmp.pop(0)-1 if tmp else h
    return

def bfs(y, x):
    global lst
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        hard = lst[y][x]
        lst[y][x]=0
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for k in range(1, hard):
            for j in range(4):
                ny, nx = y+dy[j]*k, x+dx[j]*k
                if ny>h-1 or nx>w-1 or ny<0 or nx<0: continue
                if lst[ny][nx]==0: continue
                q.append([ny, nx])
    drop_bricks()
    return  


def dfs(cnt):
    global min_total, lst, cnt_brick
    total = sum(cnt_brick)
    if total == 0:
        min_total = total
        return
    
    if cnt==n:
        if total < min_total:
            min_total = total
        return
    
    backup = deepcopy(lst)
    backup_cnt_brick = cnt_brick[:]
    for i in range(w):
        if cnt_brick[i]==0: continue # 부술 벽돌이 없는 인덱스는 스킵
        y, x = h-cnt_brick[i], i
        bfs(y, x)
        dfs(cnt+1)
        lst = deepcopy(backup)
        cnt_brick = backup_cnt_brick[:]
        

t = int(input())
for case in range(1, t+1):
    n, w, h = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(h)]
    cnt_brick = [h]*w
    min_total = 21e8
    drop_bricks()
    dfs(0)
    print(f'#{case} {min_total}')



'''
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1

1
1 12 2
1 1 1 9 1 1 0 0 1 1 1 1 
2 2 2 2 2 4 0 0 5 1 1 1 

1
1 5 5
2 0 2 0 2
2 0 2 0 2
2 0 3 0 2
2 0 2 0 2
1 0 1 0 1


1
1 5 5
2 0 2 0 2
2 0 2 0 2
2 0 2 0 2
2 0 2 0 2
1 0 3 0 1



1
4 12 15
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
'''