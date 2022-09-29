# 크루스칼 알고리즘

def union(a, b):
    global lst
    fa, fb = find(a), find(b)
    if fa==fb: return False # 사이클 존재
    lst[fb]=fa
    return True

def find(p):
    if lst[p]==p: return p
    ret = find(lst[p])
    lst[p]=ret
    return ret


t = int(input())
for case in range(1, t+1):
    v, e = map(int, input().split())
    lst = list(range(v+1))
    edge = [list(map(int, input().split())) for _ in range(e)]
    edge.sort(key=lambda x:x[2])
    total = 0
    for i in range(e):
        a, b, cost = edge[i]
        if union(a, b):
            total += cost

    print(f'#{case} {total}')


'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''