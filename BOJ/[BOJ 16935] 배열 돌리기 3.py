# 120분
import sys
input = sys.stdin.readline

def vertical_reverse(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      new_arr[i][j] = arr[N-i-1][j]
  return new_arr

def horizental_reverse(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      new_arr[i][j] = arr[i][M-j-1]
  return new_arr

def rotate_clockwise(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*N for _ in range(M)]
  for i in range(M):
    for j in range(N):
      new_arr[i][j] = arr[N-j-1][i]
  return new_arr

def rotate_reverse(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*N for _ in range(M)]
  for i in range(M):
    for j in range(N):
      new_arr[i][j] = arr[j][M-i-1]
  return new_arr

def divided_rotate_clockwise(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*M for _ in range(N)]
  n=N//2
  m=M//2
  for i in range(N):   # 2 2 0 0 3 3 1 1 2 2 0 0 3 3 1 1
    for j in range(M): # 0 1 0 1 0 1 0 1 2 3 2 3 2 3 2 3
      ny = n*((M-j-1)//m) + i%n
      nx = j%m + m*(i//n)
      new_arr[i][j] = arr[ny][nx]
  return new_arr

def divided_rotate_reverse(arr):
  N, M = len(arr), len(arr[0])
  new_arr = [[0]*M for _ in range(N)]
  n = N//2
  m = M//2
  for i in range(N):   # 0 0 2 2 1 1 3 3 0 0 2 2 1 1 3 3
    for j in range(M): # 2 3 2 3 2 3 2 3 0 1 0 1 0 1 0 1
      ny = i%n + (j//m)*n
      nx = (m*(i//n) + j%m + m)%M
      new_arr[i][j] = arr[ny][nx]
  return new_arr


N, M, R = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]
orders = list(map(int, input().rstrip().split()))
for order in orders:
  if order==1:
    A = vertical_reverse(A)
  elif order==2:
    A = horizental_reverse(A)
  elif order==3:
    A = rotate_clockwise(A)
  elif order==4:
    A = rotate_reverse(A)
  elif order==5:
    A = divided_rotate_clockwise(A)
  elif order==6:
    A = divided_rotate_reverse(A)

for a in A:
  print(*a)