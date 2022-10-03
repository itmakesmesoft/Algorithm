# (y1, x1), (y2, x2)
# 두 점사이의 거리 = ((y2-y1)**2+(x2-x1)**2)**(1/2)

def find(parent):
    if res[parent] == parent:
        return parent
    ret = find(res[parent])
    res[parent] = ret
    return ret

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb: return False
    res[fb] = fa
    return True

n = int(input())
lst = [list(map(float, input().split())) for _ in range(n)]
edge = [] # 간선 정보를 담을 리스트 생성
res = list(range(n))
for i in range(n-1):
    for j in range(i, n):
        x2, y2 = lst[j]
        x1, y1 = lst[i]
        distance = ((y2-y1)**2+abs(x2-x1)**2)**(1/2)
        edge.append([i, j, distance])
total = 0
edge.sort(key = lambda x:x[2])
for i in range(len(edge)):
    a, b, cost = edge[i]
    if union(a, b):
        total += cost
print(round(total, 2))