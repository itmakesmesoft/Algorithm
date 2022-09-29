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
t = int(input())
for case in range(1, t+1):
    n, e = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
    inf = int(21e8)
    result = [inf]*(n+1)
    heap = []
    dijkstra(0)
    print(f'#{case} {result[n]}')


'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''
