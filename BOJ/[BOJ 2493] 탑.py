import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

heap = []
result = [0]*N

for i in range(N):
    while heap:
        if heap[0][0]>lst[i]:
            result[i] = heap[0][1]+1
            break
        else:
            heapq.heappop(heap)
    heapq.heappush(heap, (lst[i], i))
print(*result)