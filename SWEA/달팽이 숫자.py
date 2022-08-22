t=int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    direct = [[0, 1],[1,0],[0,-1],[-1,0]]
    dy = dx = 0
    idx = 0
    num = 1
    for i in range(1, n**2+1):
        arr[dy][dx] = num
        y, x = dy, dx
        dy += direct[idx][0]
        dx += direct[idx][1]
        if dy>n-1 or dx > n-1 or dy < 0 or dx < 0 or arr[dy][dx]!=0:
            idx+=1
            idx%=4
            dy, dx = y, x
            dy += direct[idx][0]
            dx += direct[idx][1]  
        num+=1
    print(f'#{case}')
    for i in range(n):
        print(*arr[i])