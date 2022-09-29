n = int(input())
lst = list(map(int, input().split()))
lst = [0]+lst[:]
start, end = 0, 1
total = lst[start]+lst[end]
past = total
max_total = total
while end<=n:
    if max_total<total:
        print(start, end)
        max_total = total
    print(end)
    if past <= total:
        past = total
        end+=1
        total += lst[end]
    elif past > total:
        past = total
        if end>=n:
            break
        else:
            start, end = end+1, end+1
            total = lst[start]
print(max_total)