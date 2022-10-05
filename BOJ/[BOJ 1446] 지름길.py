import heapq
# 다익스트라

def dijkstra(start):
    heapq.heappush(heap, (0, start))  #비용, 목적지
    res[start] = 0

    while heap:
        distance, node = heapq.heappop(heap)

        if res[node] < distance: continue
        for i in lst[node]:
            


n, d = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(n):
    a,b,c = map(int, input().split())
    lst[a].append([b, c]) # lst[시작] = [도착, 비용]
inf = 21e8
res = [inf]*n
heap = []
dijkstra(0)