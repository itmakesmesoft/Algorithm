# 10분

import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())
rank = list(map(int, input().split()))

k = 1
for i in range(P):
  if i>=len(rank) or rank[i]<score:
    print(k)
    break
  elif rank[i]>score: k+=1
else:
  print(-1)