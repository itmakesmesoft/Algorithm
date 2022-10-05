def dfs(level, total):
    global max_total, used
    if total > max_total:
        max_total = total
    
    for i in range(1, n+1):
        if used[i]==1: continue
        if edge[level][i]==0: continue
        used[i]=1
        dfs(i, total+edge[level][i])
        used[i]=0

        


n = int(input())
edge = [[] for _ in range(n+1)]
for i in range(n-1): # 인접행렬 생성
    parent, child, cost = map(int, input().split())
    edge[parent].append([child, cost])
    edge[child].append([parent, cost])

max_total = -21e8
for i in range(1, n+1):
    used = [0]*(n+1)
    used[i]=1
    dfs(i, 0)
print(max_total)


'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''



# 다른 사람 풀이
# https://daegwonkim.tistory.com/269
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(node, weight):
    for w, n in tree[node]:
        if dist[n] == -1:
            dist[n] = weight + w
            dfs(n, weight + w)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([c, b])
    tree[b].append([c, a])

dist = [-1] * (n + 1)   # 간선의 합을 저장하기 위한 배열
dist[1] = 0
dfs(1, 0)   # 루트 노드를 기준으로 간선의 합이 최대 길이가 되는 리프 노드를 찾음

start = dist.index(max(dist))   # 간선의 합이 최대 길이가 되는 리프 노드
dist = [-1] * (n + 1)
dist[start] = 0 # 위에서 구한 리프 노드를 기준으로 dfs를 한 번 더 수행
dfs(start, 0)

print(max(dist))
'''