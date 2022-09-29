import heapq

def dijkstra(start):
    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > result[node]: continue
        for i in arr[node]:
            cost = dist+i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
start, end = map(int, input().split())
inf = int(21e8)
result = [inf]*n
heap = []
dijkstra(start)
print(*result)

'''

5 7
0 1 3
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3
'''