'''
test case

10 8
3
0 3
1 4
0 2
'''
def sortarr(arr):
    # 삽입정렬
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def maxrange(arr):
    arr = sortarr(arr)
    max_val = 0
    for i in range(len(arr)-1, 0, -1):
        val = arr[i]-arr[i-1]
        if val > max_val:
            max_val = val
    return max_val

width, height = map(int, input().split())
n = int(input())
ver = [0, width]
hor = [0, height]
for _ in range(n):
    axis, num = map(int, input().split())
    if axis == 0:
        hor.append(num)
    else:
        ver.append(num)
maxver = maxrange(ver)
maxhor = maxrange(hor)
print(maxhor*maxver)