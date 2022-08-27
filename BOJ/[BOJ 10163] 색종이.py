n = int(input())
arr = [[-1]*1001 for _ in range(1001)]
cnt = [0]*(n+1)
index = 0
for k in range(1, n+1):
    start_x, start_y, width, height = map(int, input().split())
    end_y = start_y+height
    end_x = start_x+width
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if arr[i][j]>0:
                index = arr[i][j]
                cnt[index] -= 1
            arr[i][j] = k
            cnt[k] += 1
for i in range(1, n+1):
    print(cnt[i])