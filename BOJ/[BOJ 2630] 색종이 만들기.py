def divide(x, y, N):
    global p_type
    if N==1 or is_same(x, y, N):
        p_type[paper[y][x]]+=1
        return
    d = N//2
    dy = [0,0,d,d]
    dx = [0,d,d,0]
    for i in range(4):
        ny, nx = dy[i]+y, dx[i]+x
        divide(nx, ny, N//2)
    

def is_same(x, y, N):
    color = paper[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if paper[i][j]!=color:
                return False
    return True


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
p_type = [0, 0]
divide(0, 0, N)
print(f'{p_type[0]}\n{p_type[1]}')