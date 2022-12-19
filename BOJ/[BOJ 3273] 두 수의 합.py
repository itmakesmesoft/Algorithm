n = int(input())
lst = list(map(int, input().split()))
x = int(input())
cnt = 0
left, right = 0, n-1
lst.sort()

while left < right:
    Sum = lst[left] + lst[right]
    if Sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif Sum > x:
        right -= 1
    elif Sum < x:
        left += 1
print(cnt)