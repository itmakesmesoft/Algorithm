def find(parent):
    if res[parent]==parent:
        return parent
    ret = find(res[parent])
    res[parent] = ret
    return ret

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb: return False
    res[fb]=fa
    return True


v, e = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(e)]
lst.sort(key = lambda x:x[2])
res = list(range(v+1))
total = 0
for i in range(e):
    a, b, cost = lst[i]
    if union(a, b):
        total += cost
print(total)