import sys
input = sys.stdin.readline

def divide(y, x, length):
    if length==1: return Map[y][x]

    new_len = length//2
    result = ""
    for i in range(2):
        for j in range(2):
            result += divide(y+i*new_len, x+j*new_len, new_len)
    if result=="1111" or result=="0000": return result[0]
    else: return "("+result+")"

N = int(input())
Map = [input() for _ in range(N)]
print(divide(0, 0, N))


# 이전 풀이
# import sys

# def divide(y, x, N): # => string
#     global result
#     if N==1 or is_same(y, x, N):
#         return Map[y][x]
#     d = N//2
#     dy = [0,0,d,d]
#     dx = [0,d,0,d]
#     result += '('
#     for i in range(4):
#         ny, nx = dy[i]+y, dx[i]+x
#         tmp = divide(ny, nx, N//2)
#         result += tmp
#     result += ')'
#     return ''


# def is_same(y, x, N): # => True or False
#     color = Map[y][x]
#     for i in range(y, y+N):
#         for j in range(x, x+N):
#             if Map[i][j] != color:
#                 return False
#     return True

# input = sys.stdin.readline
# N = int(input())
# Map = [input() for _ in range(N)]
# result = ''
# divide(0, 0, N)
# if result =='':
#     result = Map[0][0]
# print(result)

