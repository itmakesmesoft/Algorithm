N = int(input())
lst = [[" "]*N for _ in range(N)]

def recursive(y, x, num):
    global lst
    if num == 1:
        lst[y][x]="*"
        return

    for i in range(3):
        for j in range(3):
            if i==1 and j==1: continue
            ny, nx = y+(num//3)*i, x+(num//3)*j
            recursive(ny, nx, num//3)

recursive(0, 0, N)

for i in range(N):
    print(*lst[i], sep="")