import sys

def divide(y, x, N): # => string
    global result
    if N==1 or is_same(y, x, N):
        return Map[y][x]
    d = N//2
    dy = [0,0,d,d]
    dx = [0,d,0,d]
    result += '('
    for i in range(4):
        ny, nx = dy[i]+y, dx[i]+x
        tmp = divide(ny, nx, N//2)
        result += tmp
    result += ')'
    return ''


def is_same(y, x, N): # => True or False
    color = Map[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if Map[i][j] != color:
                return False
    return True

input = sys.stdin.readline
N = int(input())
Map = [input() for _ in range(N)]
result = ''
divide(0, 0, N)
if result =='':
    result = Map[0][0]
print(result)

