def moveto(y, x, d):
    global Map
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]] # Up, Down, Left, Right

    ny, nx = y+direct[d][0], x+direct[d][1]
    # if ny>R-1 or nx>C-1 or ny<0 or nx<0: return # 범위를 벗어나는 경우
    if Map[ny][nx] == '#': return # 벽인 경우

    if Map[y][x]=='w': # 캐릭터를 움직이는 경우
        if Map[ny][nx]=='b': # 이동하려는 칸이 박스인 경우
            moveto(ny, nx, d)
        if Map[ny][nx]=='.':
            Map[ny][nx], Map[y][x] = Map[y][x], Map[ny][nx]
            # chr_y, chr_x = ny, nx
    else: # 박스를 움직이는 경우
        if Map[ny][nx]=='.': # 이동하려는 칸이 빈칸인 경우
            Map[ny][nx], Map[y][x] = Map[y][x], Map[ny][nx]
    return

def find_chr():
    for i in range(R):
        for j in range(C):
            if Map[i][j] == 'w' or Map[i][j] == 'W':
                return i, j

def find_targets():
    global Map, targets
    for i in range(R):
        for j in range(C):
            if Map[i][j]=='W' or Map[i][j]=='B' or Map[i][j]=='+':
                if Map[i][j] != '+':
                    Map[i][j] = Map[i][j].lower()
                else:
                    Map[i][j] = '.'
                targets.append([i, j])

def change_to_target():
    global Map
    for i in range(len(targets)):
        y, x = targets[i]
        if Map[y][x]=='b' or Map[y][x]=='w':
            Map[y][x] = Map[y][x].upper()
        elif Map[y][x]=='.':
            Map[y][x]='+'

def is_complete():
    for i in range(len(targets)):
        y, x = targets[i]
        if Map[y][x]=='.' or Map[y][x]=='w':
            return False
    return True

k = 1
while True:
    R, C = map(int, input().split())
    if R==0 and C==0: break
    Map = [list(input()) for _ in range(R)]
    targets = []
    find_targets()
    commends = input()

    flag = 'incomplete'
    for c in commends:
        chr_y, chr_x = find_chr()
        if c=='U':
            moveto(chr_y, chr_x, 0)
        elif c=='D':
            moveto(chr_y, chr_x, 1)
        elif c=='L':
            moveto(chr_y, chr_x, 2)
        elif c=='R':
            moveto(chr_y, chr_x, 3)
        if is_complete():
            flag = 'complete'
            break
    change_to_target()
    print(f'Game {k}: {flag}')
    k+=1
    for i in range(R):
        print(*Map[i], sep='')