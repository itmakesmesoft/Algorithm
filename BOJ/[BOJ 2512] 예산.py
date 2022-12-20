def getTotal(mid):
    total = 0
    for a in lst:
        if a > mid:
            total += mid
        else:
            total += a
    return total

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst.sort()
start, end = 0, lst[N-1]
max_total = 0
result = 0

while start <=  end:
    mid = (start + end) // 2
    total = getTotal(mid)
    if total <= M:
        start = mid + 1
    elif total > M:
        end = mid - 1
        continue
    if total >= max_total:
        max_total = total
        result = mid
        
print(result)
