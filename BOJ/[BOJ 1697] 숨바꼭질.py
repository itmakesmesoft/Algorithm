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
        for n in [N*2, N+1, N-1]:
            if n < 0 or n > 100000: continue
            if memo[n]==1: continue
            memo[n]=1
            q.append([n, t+1])
memo = [0]*100001
print(bfs(N, K))