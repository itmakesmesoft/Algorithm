'''
test case

160
57
0322
92
48
0 3
'''

arr = [list(input()) for _ in range(5)]
line = list(map(int, input().split()))
for i in range(2):
    idx = line[i]
    min_val = 0
    for j in range(len(arr[idx])):
        if arr[idx][0]>arr[idx][j]:
            arr[idx][0], arr[idx][j] = arr[idx][j], arr[idx][0]
for i in range(5):
    print(arr[i][0], end=' ')
        