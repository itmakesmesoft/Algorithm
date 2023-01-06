from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    global cnt
    t = 0
    q = deque()
    q.append([N, t])
    while q:
        N, t = q.popleft()
        if N == K: return t
        if N < 0: continue
        if memo[N] > t: memo[N] = t
        if N*2 < 100000 and memo[N*2] > t+1:
            q.append([N*2, t+1])
            cnt+=1
        if N+1 < 100000 and memo[N+1] > t+1:
            q.append([N+1, t+1])
            cnt+=1
        if N-1 < 100000 and memo[N-1] > t+1:
            q.append([N-1, t+1])
            cnt+=1
INF = int(21e9)
cnt = 0
memo = [INF]*100001
print(bfs(N, K))
print(cnt)