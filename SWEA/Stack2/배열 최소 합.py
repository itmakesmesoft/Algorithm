def dfs(level, total):
    global min_total
    if total > min_total: # 시간 초과 방지. 합계가 최소합보다 클 경우 종료
        return
    if level == n:
        if min_total > total:
            min_total = total
        return
    for i in range(n):
        if visited[i]==0: # 방문 여부 확인
            visited[i]=1
            dfs(level+1, total + arr[level][i])
            visited[i]=0



t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    min_total = float('inf')
    dfs(0, 0)
    print(f'#{case} {min_total}')


'''
test case
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''