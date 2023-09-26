import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(input().rstrip()) for _ in range(N)]
B = [list(input().rstrip()) for _ in range(N)]

def is_same():
    for i in range(N):
        for j in range(M):
            if A[i][j]!=B[i][j]: return False
    return True

def change(y, x):
    global A
    for i in range(y, y+3):
        for j in range(x, x+3):
            A[i][j] = '0' if A[i][j]=='1' else '1'
    return

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            count += 1
            change(i, j)

if is_same():
    print(count)
else:
    print(-1)
