import sys
input = sys.stdin.readline

def conquer(y, x, g):
    global answer
    if N==1:
        answer[Map[y][x]+1]+=1
        return
    elif g == 1: return Map[y][x]
    result = [0]*3
    gap = g//3
    for i in range(y, y+g, gap):
        for j in range(x, x+g, gap):
            res = conquer(i, j, gap)
            if res == -2: continue
            else: result[res]+=1
    for i in range(-1, 2):
        if result[i]==9 or (N==1 and result[i]==1):
            if g==N: answer[i+1]+=1
            return i
    for i in range(-1, 2): # 숫자 세기
        answer[i+1] += result[i]
    return -2


N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

answer = [0]*3
conquer(0, 0, N)

print(*answer, sep="\n")




# 이전 풀이

# N = int(input())
# Map = [list(map(int, input().split())) for _ in range(N)]
# result = [0]*3

# def divide(y, x, step):
#   global result
#   if step==0:
#     return Map[y][x]

#   busket = [0]*9
#   flag = True
#   for i in range(3):
#     for j in range(3):
#       busket[i*3+j] = divide(y+step*i, x+step*j, step//3)

#       if i==0 and j==0: continue
#       elif busket[i*3+j]!=busket[i*3+j-1]:
#         flag = False

#   # 다른 경우 카운트
#   # 같은 경우에는 카운트하지 않고 반복되는 해당 수를 반환
#   if flag and busket[0]!=-2:
#     return busket[0]
#   else:
#     for i in range(9):
#       if busket[i]!=-2:
#         result[busket[i]+1]+=1
#     return -2
# if N>=3:
#   res = divide(0, 0, N//3)
#   if res!=-2:
#     result[res+1]+=1
# else: result[Map[0][0]+1]+=1
# for i in range(3):
#   print(result[i])


# '''
# 1
# 1

# 3
# -1 -1 -1
# -1 -1 -1
# -1 -1 -1
# '''