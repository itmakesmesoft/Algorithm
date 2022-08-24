n = int(input())
arr = [input() for _ in range(n)]
count = [0]*n
for i in range(n):
    count[i] = len(arr[i])

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if count[j]<count[min_idx]:
            min_idx = j
        elif count[min_idx]==count[j]:
            if arr[min_idx]>arr[j]:
                min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    count[i], count[min_idx] = count[min_idx], count[i]

for i in range(n):
    print(arr[i])