def find_stone(y, x, dir, stone):
    global plate
    if plate[y][x]==stone: return True
    ny, nx = y+dy[dir], x+dx[dir]
    if ny>n-1 or nx>n-1 or ny<0 or nx<0: return False
    if find_stone(ny, nx, dir, stone):
        plate[ny][nx]=stone
        find_dir(ny, nx, stone)

def find_dir(y, x, stone):
    global plate
    for i in range(8):
        k = 1
        while True:
            ny, nx = y+dy[i]*k, x+dx[i]*k
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: break
            if plate[ny][nx]==stone%2+1:
                find_stone(ny, nx, i, stone)
            k+=1


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    plate = [[0]*n for _ in range(n)]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    cnt = [0, 2, 2]

    # 초기값 세팅
    init_val = n//2-1
    for i in range(2):
        for j in range(2):
            if i==j: 
                plate[init_val+i][init_val+j]=2
            else: 
                plate[init_val+i][init_val+j]=1
    
    for i in range(m):
        x, y, stone = map(int, input().split())
        x, y = x-1, y-1 
        plate[y][x] = stone
        find_dir(y, x, stone)
    print(plate)



    

'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''