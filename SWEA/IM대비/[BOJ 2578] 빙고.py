'''
test case

11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
def isbingo():
    total = 0
    isdiagonal1 = isdiagonal2 = True
    for i in range(5): #가로 조사
        isrow = iscol = True
        for j in range(5):
            if guest[i][j]!=0: # 가로 빙고가 아닌 경우 False
                isrow = False
            if guest[j][i]!=0: # 세로 빙고가 아닌 경우 False
                iscol = False
        total += (isrow + iscol)
        if guest[i][4-i]!=0: # 우상좌하 대각선 빙고가 아닌 경우 False
            isdiagonal1 = False
        if guest[i][i]!=0:   # 좌상우하 대각선 빙고가 아닌 경우 False
            isdiagonal2 = False
    total += (isdiagonal1 + isdiagonal2)
    return total

guest = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]
bucket = [0]*26
for i in range(5): # 버킷에 guest 원소 좌표 저장 (for문을 여러번 돌릴 필요 없이 좌표를 찾기 위함)
    for j in range(5):
        bucket[guest[i][j]]=[i, j]

for i in range(5):
    for j in range(5):
        number = host[i][j]
        y, x = bucket[number] # 버킷에서 좌표값을 찾아 원소 값을 0으로 변경 
        guest[y][x]=0
        result = isbingo() # 빙고 갯수를 반환
        if result >= 3:
            count = i*5 + j+1
            break
    if result >= 3:
        break
print(count)