t = int(input())
for case in range(1, t+1):
    n = int(input()) # 높이
    arr = list(map(int, input().split()))
    max_k = 0
    for i in range(n):
        cnt = 0 # arr[i]보다 작은 오른쪽 원소의 갯수
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt+=1
        if max_k < cnt:
            max_k = cnt
    print(f'#{case} {max_k}')