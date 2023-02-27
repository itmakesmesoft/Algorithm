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




# import sys
# input = sys.stdin.readline

# def dfs(num):
#     global used
#     for i in range(N):
#         if used[i]==0 and Map[num][i]==1:
#             used[i]=1
#             dfs(i)

# N, M = map(int, input().split())
# Map = [[0]*N for _ in range(N)]
# used = [0]*N
# for _ in range(M):
#     a, b = map(int,input().split())
#     Map[a-1][b-1] = Map[b-1][a-1] = 1

# cnt = 0
# for i in range(N):
#     if used[i]==0:
#         used[i]=1
#         dfs(i)
#         cnt+=1
# print(cnt)