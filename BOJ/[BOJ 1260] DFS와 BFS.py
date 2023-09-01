import sys, collections
input = sys.stdin.readline

def dfs(level):
    global visited
    print(level+1, end=" ")
    for i in range(N):
        if lst[level][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)
    return


def bfs(y):
    global visited
    q = collections.deque()
    q.append(y)
    while q:
        y = q.popleft()
        print(y+1, end=" ")
        for i in range(N):
            if lst[y][i]==1 and visited[i]==0:
                visited[i]=1
                q.append(i)
    return



N, M, V = map(int, input().split())
lst = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a-1][b-1] = lst[b-1][a-1] = 1
visited = [0]*N
visited[V-1]=1
dfs(V-1)
print()
visited = [0]*N
visited[V-1]=1
bfs(V-1)

