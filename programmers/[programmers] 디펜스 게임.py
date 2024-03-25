import heapq
def solution(n, k, enemy):
    heap = []
    i = -1
    total = 0
    while total <= n and i<len(enemy)-1:
        i+=1
        total += enemy[i]
        heapq.heappush(heap, enemy[i] * -1)
        if total > n and k>0:
            k-=1
            total += heapq.heappop(heap)
    if total <= n: i+=1
    return i