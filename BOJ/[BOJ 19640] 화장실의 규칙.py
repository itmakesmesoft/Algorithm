# 우선순위 큐 이용해야 함
import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
me = [0, 0, 0, 0]
heap = []
lines = [deque() for _ in range(M)]

for i in range(N):
    d, h = map(int , input().split())
    if i==K:
        me = [-1*d, -1*h, i%M, i]
    if i<M:
        heapq.heappush(heap, (-1*d, -1*h, i%M, i))
    else:
        lines[i%M].append((-1*d, -1*h, i%M, i))

count = 0
while heap:
    d, h, col, index  = heapq.heappop(heap)
    if d==me[0] and h==me[1] and col==me[2] and index ==me[3]:
        break
    else:
        if lines[col]:
            heapq.heappush(heap, lines[col].popleft())
    count+=1
print(count)

# N, M, K = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]
# my_d, my_h = lst[K][0], lst[K][1]
# count = 0
# indexes = list(range(M))

# # indexes는 스택과 같은 방식으로 작동
# # indexes[i] 다음 인덱스 -> indexes[i+M]
# # i==K%M인 경우(즉, 같은 줄에 서 있는 경우)
# # i==K%M이고, indexes[i]==K인 경우 => 자신의 차례인 경우 => break
# for _ in range(N//M+1):
#   for i in range(M):
#     print(indexes)
#     index = indexes[i]
#     d, h = lst[index]
#     if d>my_d:
#       count+=1
#       indexes[i] += M
#     elif d==my_d and h>my_h:
#       count+=1
#       indexes[i] += M
#     elif d==my_d and h==my_h:
#       if i<K%M:
#         count+=1
#         indexes[i] += M
#       elif i==K%M and index != K:
#         count+=1
#         indexes[i] += M
#       elif i==K%M and index == K:
#         break
# print(count)

#
# 6 2 2
# 1500 100
# 1500 500
# 1500 400
# 1500 400
# 1500 200
# 1500 500
# 답 : 4

# 3 2 1
# 100 100
# 100 100
# 100 100
# 답 : 2


# 3 2 2
# 100 100
# 100 100
# 100 100
# 답 : 1