import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def union(a, b):
    global lst
    fa, fb = find(a), find(b)
    if fa==fb: return False
    lst[fb] = fa

def find(c):
    global lst
    if lst[c]==c: return c
    ret = find(lst[c])
    lst[c] = ret
    return ret


N, M = map(int, input().split())
lst = list(range(N+1))

for _ in range(M):
    req, a, b = map(int, input().split())
    if req: # 포함 여부 확인
        fa, fb = find(a), find(b)
        if fa==fb:
            print("YES")
        else:
            print("NO")
    else: # 합집합 연산
        if a>b: a,b = b,a
        union(a, b)