import heapq, sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:x[0], reverse=True)
heap = []
max_length = 0
while lst:
    cur_st, cur_ed = lst.pop()
    if heap:
        ed, st = heapq.heappop(heap)
        if ed>cur_st: # 시간이 겹치는 경우
            heapq.heappush(heap, [ed, st]) # 기존 강의실 추가
    heapq.heappush(heap, [cur_ed, cur_st]) # 새로운 강의실 추가
    if len(heap)>max_length:
        max_length = len(heap)
print(max_length)