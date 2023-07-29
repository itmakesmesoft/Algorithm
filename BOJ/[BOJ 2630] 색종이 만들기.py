# 분할 정복
# 가로 1/2, 세로 1/2
import sys
input = sys.stdin.readline

def is_possible(st_y, st_x, length):
    global blue, white
    if length==1: return Map[st_y][st_x]
    else: # 재귀 구조
        new_length = length//2
        b = w = 0
        for i in range(2):
            for j in range(2):
                res = is_possible(st_y+i*new_length, st_x+j*new_length, new_length)
                if res==1: b+=1
                elif res==0: w+=1
        if length==N and (b==4 or w==4):
            blue += b//4
            white += w//4
        elif b==4 or w==4:
            return 1 if b==4 else 0
        else:
            blue += b
            white += w
            return -1

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

blue = white = 0
is_possible(0, 0, N)

print(white) # 햐얀색 색종이 갯수
print(blue) # 파란색 색종이 갯수

# def divide(x, y, N):
#     global p_type
#     if N==1 or is_same(x, y, N):
#         p_type[paper[y][x]]+=1
#         return
#     d = N//2
#     dy = [0,0,d,d]
#     dx = [0,d,d,0]
#     for i in range(4):
#         ny, nx = dy[i]+y, dx[i]+x
#         divide(nx, ny, N//2)


# def is_same(x, y, N):
#     color = paper[y][x]
#     for i in range(y, y+N):
#         for j in range(x, x+N):
#             if paper[i][j]!=color:
#                 return False
#     return True


# N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
# p_type = [0, 0]
# divide(0, 0, N)
# print(f'{p_type[0]}\n{p_type[1]}')