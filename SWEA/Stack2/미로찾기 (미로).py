def bfs(y, x, cnt):
    queue = [0]
    while queue:
        q = queue.pop(0)
        if q not in visited:
            visited.append(q)
            for a in arr[q]:
                if v


t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []

'''
1
5
13101
10101
10101
10101
10021
'''