# N = int(input())
# lst = list(map(int, input().split()))
# res = [0]*N

# for i in range(N):
#     count = 0
#     for j in range(N):
#         if res[j]==0:
#             if count == lst[i]:
#                 res[j]=i+1
#                 break
#             else:
#                 count+=1
# print(*res)


# 10분

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

result = [0]*N
for i in range(N):
  k = 0
  for j in range(N):
    if result[j] == 0:
      if k == lst[i]:
        result[j] = i+1
        break
      k += 1
print(*result)