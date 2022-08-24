def dfs(start, cnt):
    global min_cnt
    if min_cnt!= -1 and min_cnt < cnt:
        return
    if start == end:
        if min_cnt > cnt or min_cnt == -1:
            min_cnt = cnt
        return
    for i in range(v):
        if arr[start][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i, cnt+1)
            visited[i]=0

t = int(input())
for case in range(1, t+1):
    v,e = map(int, input().split()) # v는 노드 갯수, e는 간선 갯수
    arr = [[0]*v for _ in range(v)]
    for i in range(e):
        a,b = map(int, input().split())
        arr[a-1][b-1]=arr[b-1][a-1]=1 # 간선은 방향성이 없으므로, 양방향 모두 1로 저장

    start, end = map(int, input().split())
    start, end = start-1, end-1
    min_cnt = -1
    visited = [0]*v
    visited[start] =1 
    dfs(start, 0)
    if min_cnt == -1:
        min_cnt = 0
    print(f'#{case} {min_cnt}')


'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''