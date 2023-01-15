import heapq
import sys

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    value = int(input())
    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
        continue
    heapq.heappush(heap, (abs(value), value))