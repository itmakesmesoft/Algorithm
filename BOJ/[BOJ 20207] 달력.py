import heapq

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[0], x[1]*-1))
answer = 0
height = 1
heap = []
heapq.heappush(heap, [lst[0][1]+1, lst[0][0]])
min_st, max_ed = lst[0][0], lst[0][1]+1

for i in range(1, N):
    start, end = lst[i]
    if heap:
        prev_ed, prev_st = heap[0]
        if prev_ed>start:
            height+=1
        elif prev_ed<=start:
            if max_ed<start:
                heap = []
                answer += ((max_ed - min_st)*height)
                height = 1
                min_st = start
            else:
                heapq.heappop(heap)
    heapq.heappush(heap, [end+1, start])
    if max_ed < end+1: max_ed = end+1
if heap: answer += ((max_ed-min_st)*height)
print(answer)