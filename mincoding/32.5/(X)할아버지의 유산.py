def Sum(start_x, start_y, end_x, end_y):
    print(start_x, start_y, end_x, end_y)
    total = 0
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            total += arr[i][j]
    print(total)
    return total

def rect(y, x):
    end_y, end_x = y, x
    for i in range(8-x):
        for j in range(4-y):
            ny, nx = y+j, x+i
            print(f'nx={nx} ny={ny}')
            if arr[ny][nx]==0:
                print(f'end_y {end_y}')
                if end_y>ny:
                    print(x, y, end_x, end_y)
                    result.append(Sum(x, y, end_x, end_y))
                    end_y, end_x = ny, nx
                    return
                elif end_y<=ny:
                    end_x=nx+1
                    break
            elif arr[ny][nx]!=0:
                end_y, end_x = ny+1, nx+1
    result.append(Sum(x, y, end_x, end_y))
            # elif ny==4 and nx==3:

    print(result)
    print("종료")

arr = [list(map(int, input().split())) for _ in range(4)]
result = []
for i in range(4):
    for j in range(8):
        if arr[i][j] != 0:
            rect(i, j)
print(result)
# max_num = 0
# for i in range(len(result)):
#     if max_num < result[i]:
#         max_num = result[i]
# print(max_num)


'''
test case
0 0 3 3 0 0 0 0
5 1 4 2 6 9 8 1
6 5 1 3 2 6 3 2
0 0 0 0 9 9 4 0
'''