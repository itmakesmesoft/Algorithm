import sys

def check_queen(level, i):
    if level + i == 

def dfs(level):
    global count, MAP
    if level == N:
        count += 1
        return

    for i in range(N):
        if check_queen(level, i):
            MAP[level][i]=1
            dfs(level+1)
            MAP[level][i]=0

input = sys.stdin.readline
N = int(input())
MAP = [[0]*N for _ in range(N)]
count = 0
dfs(0)
print(count)