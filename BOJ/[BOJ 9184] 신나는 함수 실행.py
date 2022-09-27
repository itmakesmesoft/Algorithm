# def w(a, b, c):
#     global memo
#     if a<=0 or b<=0 or c<=0:
#         return memo[0][0][0]
#     elif a>20 or b>20 or c>20:
#         memo[20][20][20] = w(20, 20, 20)
#         return memo[20][20][20]
#     elif a<b and b<c:
#         memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         return memo[a][b][c]
#     else:
#         memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
#         return memo[a][b][c]

import sys

def w(a, b, c):
    global memo
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if memo[a][b][c]:
        return memo[a][b][c]
    if a<b and b<c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]
    memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]

memo = [[[0]*21 for _ in range(21)] for _ in range(21)] # 범위를 21로 해도 되는 이유는, 음수일 경우 무조건 1을 반환하도록 구현하기 때문
a = b = c = 0
while True: 
    a, b, c = map(int,sys.stdin.readline().split()) # 속도 향상을 위해 readline 입력 메서드 사용
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')