arr = [1,5,4,2,-5,-7]
n = int(input())
# 1 5 4 2 -5 -7
# 선택정렬
for i in range(len(arr)-1):
    max_j = i
    for j in range(i+1, len(arr)):
        if arr[j]>arr[max_j]:
            max_j = j
    arr[max_j], arr[i] = arr[i], arr[max_j]
print(arr[n-1])