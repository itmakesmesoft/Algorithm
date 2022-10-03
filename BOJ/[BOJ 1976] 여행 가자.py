def find(parent):
    if res[parent]==parent:
        return parent
    ret = find(res[parent])
    res[parent] = ret
    return ret

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb: return
    res[fb] = fa


n = int(input()) # 도시 수
m = int(input()) # 여행 계획에 속한 도시 수
lst = [list(map(int, input().split())) for _ in range(n)]
res = list(range(n))
for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            if i > j: a, b = j, i
            else: a, b = i, j
            union(a, b)

flag = 1
plan = list(map(int, input().split()))
past_parent = find(plan[0]-1)
for i in plan:
    if find(i-1)!=past_parent:
        flag = 0
        break
if flag:
    print("YES")
else:
    print("NO")

'''



'''