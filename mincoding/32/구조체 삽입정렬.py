'''
# 삽입정렬
# 3,1,5,4
arr = [3,1,5,4]
for i in range(len(arr)):
    for j in range(i, 0, -1):
        if arr[j]<arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
print(arr)
'''

n = int(input())
arr = [list(input().split()) for _ in range(n)]
for i in range(n):
    for j in range(i, 0, -1):
        if arr[j][0]<arr[j-1][0]: # 0번 인덱스끼리 비교
            arr[j], arr[j-1] = arr[j-1], arr[j]
        elif arr[j][0] == arr[j-1][0]: # 0번 인덱스가 같은 경우 
            if arr[j][1]<arr[j-1][1]: # 1번 인덱스와 비교
                arr[j], arr[j-1] = arr[j-1], arr[j]

for i in range(n): # 출력
    print(*arr[i])