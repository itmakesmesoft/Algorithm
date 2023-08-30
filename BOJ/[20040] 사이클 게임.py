import sys
input = sys.stdin.readline

def find(node):
    if lst[node]==node: return node
    ret = find(lst[node])
    return ret

def union(a, b):
    fa, fb = find(a), find(b)
    if fa==fb: return True
    lst[fb]=fa

N, M = map(int, input().split())
lst = list(range(N))
answer = 0
for i in range(M):
    a, b = map(int, input().split())
    if a>b: a,b = b,a
    res = union(a, b)
    if res and answer==0: answer = i+1

print(answer)