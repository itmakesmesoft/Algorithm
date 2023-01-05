N, M = map(int, input().split())
INF = 21e8
MAP = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = MAP[b][a] = 1

for via in range(N+1): 
    for start in range(N+1):
        for end in range(N+1):
            if MAP[start][end] > MAP[start][via] + MAP[via][end]:
                MAP[start][end] = MAP[start][via] + MAP[via][end]
min_sum = INF
min_index = 0
for i in range(1, N+1):
    s = sum(MAP[i][1:])
    if s < min_sum:
        min_sum = s
        min_index = i
print(min_index)