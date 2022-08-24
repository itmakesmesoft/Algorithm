def isptn(y):
    for j in range(5):
        if string[y][j]!=ptn[j]:
            return False
    return True

string = [list(input()) for _ in range(5)]
for i in range(5): # 배열 1열 3열 변경
    string[i][1], string[i][3] = string[i][3], string[i][1]
flag = 0
ptn = 'MAPOM'
for i in range(5):
    if isptn(i):
        flag = 1
if flag:
    print("yes")
else:
    print("no")