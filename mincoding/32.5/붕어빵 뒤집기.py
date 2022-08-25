def flip(y, x):
    dy = [0,1,0,-1,0]
    dx = [1,0,-1,0,0]
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny>2 or nx>5 or ny<0 or nx<0:
            continue
        if res[ny][nx]=='#':
            res[ny][nx]=arr[ny][nx]
        else:
            res[ny][nx]='#'
    return

arr = [['A','B','C','E','F','G'],['H','I','J','K','L','M'],['N','O','P','Q','R','S']]
res = [['A','B','C','E','F','G'],['H','I','J','K','L','M'],['N','O','P','Q','R','S']]
inputs = list(input())
for i in range(3):
    for j in range(6):
        for k in range(len(inputs)):
            if arr[i][j]==inputs[k]:
                flip(i, j)
for i in range(3):
    for j in range(6):
        print(res[i][j], end='')
    print()