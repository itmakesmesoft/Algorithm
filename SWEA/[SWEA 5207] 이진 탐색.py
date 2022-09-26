def binary(num):
    start, end = 0, n-1
    status = 0 # -1: 왼쪽, 1: 오른쪽, 0: 초기값
    while start<=end:
        mid = (start+end)//2
        if a[mid]>num:
            if status == -1:
                return 0
            end = mid-1
            status = -1
        elif a[mid]<num:
            if status == 1:
                return 0
            start = mid+1
            status = 1
        else: # a[mid]==num
            return 1
    return 0

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(m):
        if binary(b[i]):
            cnt+=1
    print(f'#{case} {cnt}')


'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''