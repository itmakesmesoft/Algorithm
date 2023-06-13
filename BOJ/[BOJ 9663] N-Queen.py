# import sys

# def check_queen(level, i):
#     direct = [-1, 0, 1]
#     for j in range(level):
#         for k in range(3):
#             nx = i+direct[k]*(level-j)
#             if nx>N-1 or nx<0: continue
#             if MAP[j][nx]==1: return False
#     return True

# def dfs(level):
#     global count, visited, MAP
#     if level == N:
#         count += 1
#         return

#     for i in range(N):
#         if check_queen(level, i):
#             MAP[level][i]=1
#             dfs(level+1)
#             MAP[level][i]=0

# input = sys.stdin.readline
# N = int(input())
# MAP = [[0]*N for _ in range(N)]
# count = 0
# dfs(0)
# print(count)


import sys
input = sys.stdin.readline

def is_promising(row, col): # -> True/False
  for i in range(0, row):
    if col==rows[i]: return False
    if rows[i]>-1 and abs(rows[i]-col)==abs(i-row): return False
  return True

def dfs(row):
  global count, rows
  if row==N:
    count+=1
    return
  for i in range(N):
    if is_promising(row, i):
      rows[row]=i
      dfs(row+1)

N = int(input())
rows = [-1]*N
count = 0
dfs(0)
print(count)