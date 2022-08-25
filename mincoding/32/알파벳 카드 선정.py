'''
test case

ZZAYYYKBTA
6
'''

arr = list(input())
n = int(input())

# 삽입 정렬
k = len(arr)
for i in range(k):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

# 뒤에서 n만큼 슬라이싱
arr = arr[k-n:]

# 빈도수 높은 알파벳 탐색
bucket = [0]*26
max_idx = 0
for i in range(n):
    idx = ord(arr[i])-65
    bucket[idx] += 1
    if bucket[idx]>bucket[max_idx]:
        max_idx = idx
alpha = chr(max_idx+65)
print(alpha)