

'''
test case
0 0 3 3 0 0 0 0
5 1 4 2 6 9 8 1
6 5 1 3 2 6 3 2
0 0 0 0 9 9 4 0

0 0 3 3 0 0 1 1
2 1 1 2 0 0 2 2
1 1 2 3 9 1 3 3
0 0 1 1 0 0 4 4
'''
def range_sum(start_x, start_y, end_x, end_y):
    global max_total
    total = 0
    for i in range(start_y, end_y+1):
        for j in range(start_x, end_x+1):
            total += arr[i][j]
    if total > max_total: # 최댓값 갱신
        max_total = total

def search_range(y, x):
    end_y, end_x = y, x
    for i in range(8-x):
        for j in range(4-y):
            ny, nx = y+j, x+i
            if arr[ny][nx]!=0:   # 아래로 탐색 중 0이 아닌 경우
                if nx == x:      # 만약 첫번째 y축 탐색인 경우
                    end_y = ny
                else:            # 첫번째 x축이 아닌경우, end_x를 갱신
                    end_x = nx
            elif arr[ny][nx]==0: # 아래로 탐색 중 0을 만난 경우
                if end_y > ny-1: # end_y값이 현재값-1보다 큰 경우 이전 end_y에서의 범위의 합을 구함
                                 # ny-1을 하는 이유 : 현재 ny에서의 원소는 0이므로, end_y와의 비교대상은 ny-1이 되어야 함.
                    range_sum(x, y, end_x, end_y)
                    end_y, end_x = ny, nx # end 갱신
                    return
                elif ny == y:    # 시작 y좌표에서 0을 만난 경우
                    range_sum(x, y, end_x, end_y)
                    return
            if ny == 3 and nx == 7: # 좌표 끝이면서, 원소가 0이 아닌경우 범위의 합을 구함
                range_sum(x, y, end_x, end_y)

arr = [list(map(int, input().split())) for _ in range(4)]
max_total = 0
for i in range(4):
    for j in range(8):
        if arr[i][j] != 0: search_range(i, j)
print(max_total)

