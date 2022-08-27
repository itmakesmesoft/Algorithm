'''
test case

4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
'''

def throw(curr_y, curr_x): # 동쪽: 1, 서쪽: 2, 북쪽: 3, 남쪽: 4
    global dice_fb, dice_lr
    if d==0: 
        # 동쪽 이동
        dice_lr.insert(0, dice_lr.pop())
        dice_fb[1]=dice_lr[1]
        
    elif d==1:
        # 서쪽 이동
        dice_lr.append(dice_lr.pop(0))
        dice_fb[1]=dice_lr[1]

    elif d==2:
        # 북쪽 이동
        dice_fb.append(dice_fb.pop(0))
        dice_lr[1], dice_lr[3] = dice_fb[1], dice_fb[3]
    else:
        # 남쪽 이동
        dice_fb.insert(0, dice_fb.pop())
        dice_lr[1], dice_lr[3] = dice_fb[1], dice_fb[3]
    dice_lr[3] = dice_fb[3] = Map[curr_y][curr_x]
    return dice_fb[1] # 윗면 값 반환


n, m, x, y, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))  # 동쪽: 1, 서쪽: 2, 북쪽: 3, 남쪽: 4
dice_fb = [0,0,0,0]
dice_lr = [0,0,0,0]
'''
      4 <- 북
서  1 2 3  동 (2: 위)
      5 <- 남 
      6 <- 밑
                                dice_fb = [4,2,5,6]
                                dice_lr = [1,2,3,6]
'''
for i in range(n):
    for j in range(m):
        if Map[i][j]==0:
            startpoint = (i, j) # y, x
            curr_y, curr_x = startpoint[:]
            break
        
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for i in range(len(orders)):
    d = orders[i]-1
    ny = curr_y + dy[d]
    nx = curr_x + dx[d]
    if ny>n-1 or nx>m-1 or ny<0 or nx<0: continue
    curr_y, curr_x = ny, nx
    value = throw(curr_y, curr_x) # 윗면 값
    print(value)
