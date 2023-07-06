import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
heapq.heapify(lst)
total = 0
while len(lst)>1:
    num = heapq.heappop(lst) + heapq.heappop(lst)
    total += num
    heapq.heappush(lst, num)
print(total)