from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def bfs(y, x):
    return


cntTable = [0]*7
for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            cur_y, cur_x = i, j
        elif arr[i][j]>0:
            cntTable[arr[i][j]]+=1
q = deque()
for i in range(1, 7):
    for j in range(cntTable[i]):
        if j==i+1: break
        q.append(i)