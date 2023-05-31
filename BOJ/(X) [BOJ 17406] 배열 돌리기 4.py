from copy import deepcopy

N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]


def rotate(r, c, s):
    global Map
    for i in range(N):
        for j in range(M):
            if i == j:
                pass


for _ in range(K):
    r, c, s = map(int, input().split())
    rotate(r, c, s)
print(Map)
