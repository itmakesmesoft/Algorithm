arr = [list(map(int, input().split())) for _ in range(4)] # 4*8
left_top, right_bottom = [7,3], [0,0]
for i in range(4):
    for j in range(8):
        if arr[i][j]>0 and left_top[0]==i and left_top[1]<=j:
            for k in range(4-i):
                if arr[k][j]==0:
                    break
                else:
                    right_bottom=k
