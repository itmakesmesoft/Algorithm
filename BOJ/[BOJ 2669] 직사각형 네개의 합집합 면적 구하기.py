arr = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(4):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if arr[i][j] == 0:
                arr[i][j]=1
                cnt += 1
print(cnt)