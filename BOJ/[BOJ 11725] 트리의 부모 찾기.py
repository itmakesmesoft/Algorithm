'''
## dfs 풀이
def dfs(level):
    global visited, result
    for i in range(1, n+1):
        if edge[level][i]==0: continue
        if visited[level][i]==1: continue
        if i!=level and edge[level][i]==1:
            visited[level][i]=1
            dfs(i)
            result[i]=level

n = int(input())
edge = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    edge[a][b] = edge[b][a] = 1
visited = [[0]*(n+1) for _ in range(n+1)]
result = [0]*(n+1)
dfs(1)
for i in range(2, n+1):
    print(result[i])
'''

## bfs 풀이

from collections import deque
import sys
input = sys.stdin.readline

def bfs(level):
    visited = [0]*(n+1)
    visited[1]=1
    q = deque([level])
    while q:
        now = q.popleft()
        for i in edge[now]:
            if visited[i]==1: continue
            result[i]=now
            q.append(i)
            visited[i]=1
    return result

n = int(input())
edge = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

result = [0]*(n+1)
bfs(1)
for i in range(2, n+1):
    print(result[i])