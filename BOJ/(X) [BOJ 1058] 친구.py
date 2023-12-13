import sys
input = sys.stdin.readline

def dfs(cur, level):
  global max_friends
  if level==2: return
  for i in range(N):
    if lst[cur][i]=='Y' and friends[i]==0:
      friends[i] = 1
      dfs(i, level+1)

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
max_friends = 0
for i in range(N):
  friends = [0]*N
  friends[i]=1
  dfs(i, 0)
  max_friends = max(max_friends, sum(friends))
print(max_friends-1)

# dfs로는 불가능
# https://hwayomingdlog.tistory.com/139

