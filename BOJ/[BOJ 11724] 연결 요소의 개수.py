# Union find로 시도 -> 실패

import sys
input = sys.stdin.readline

def union(a, b):
  global edge
  fa, fb = find(a), find(b)
  if fa == fb: return False #  이미 같은 그룹
  if fb > fa:
    edge[fb] = fa
  else:
    edge[fa] = fb
  return True


def find(node):
  global edge
  if edge[node] == node: return node
  ret = find(edge[node])
  edge[node] = ret
  return ret

N, M = map(int, input().split())
edge = list(range(N+1))
cnt = 0
for _ in range(M):
  a, b = map(int, input().split())
  if union(a, b):
    cnt += 1

print(N - cnt)




# BFS 시도
# from collections import deque
# import sys

# input = sys.stdin.readline

# def bfs(num):
#   global visited
#   q = deque()
#   q.append(num)
#   while q:
#     num = q.popleft()
#     for i in range(1, N+1):
#       if visited[i]==0 and Map[num][i] == 1:
#         visited[i]=1
#         q.append(i)

# N, M = map(int, input().split())
# Map = [[0]*(N+1) for _ in range(N+1)]
# visited = [0]*(N+1)


# for _ in range(M):
#   a, b = map(int, input().split())
#   Map[a][b] = Map[b][a] = 1
# cnt = 0
# for i in range(1, N+1):
#   if visited[i]==0:
#     visited[i]=1
#     bfs(i)
#     cnt+=1
# print(cnt)