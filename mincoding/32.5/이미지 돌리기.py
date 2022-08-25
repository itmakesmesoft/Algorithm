n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(k):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-j-1][i]
    arr = tmp
for i in range(n):
    print(*arr[i])

'''
test case

5 1
1 0 1 0 1
1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
0 1 0 1 0
'''