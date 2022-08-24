t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = m%n
    print(f'#{case} {arr[idx]}')