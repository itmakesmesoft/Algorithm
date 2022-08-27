n = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(n):
    x, y = map(int, input().split()) # 위아래 반전 상관 무
    for i in range(10):
        for j in range(10):
            if arr[y+i][x+j]==0:
                 arr[y+i][x+j]=1
                 cnt += 1
print(cnt)
           

    