def rotate(index, clockwise):
    # print(f'{index}번 톱니바퀴, {clockwise}방향 호출됨됨')
    global gears, rotated
    if index>0 and gears[index-1][2] != gears[index][6] and rotated[index-1]==0:
        rotated[index-1] = 1
        rotate(index-1, -1 if clockwise>0 else 1)
    if index<3 and gears[index+1][6] != gears[index][2] and rotated[index+1]==0:
        rotated[index+1]=1
        rotate(index+1, -1 if clockwise>0 else 1)
    if clockwise==1:
        gears[index] = gears[index][7]+gears[index][:7]
    else:
        gears[index] = gears[index][1:]+gears[index][0]

gears = [input() for _ in range(4)]
K = int(input())
orders = [list(map(int, input().split())) for _ in range(K)]

for index, clockwise in orders:
    rotated = [0]*4
    rotated[index-1] = 1
    rotate(index-1, clockwise)

score = 0
for i in range(4):
    if gears[i][0]=='1':
        score+=2**i
print(score)