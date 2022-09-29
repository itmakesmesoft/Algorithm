def union(a, b):
    fa, fb = find(a), find(b)
    if fa==fb: return False
    arr[fb] = fa
    return True

def find(p):
    if arr[p]==p: return p
    ret = find(arr[p])
    arr[p] = ret
    return ret

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(range(n+1))
    lst = list(map(int, input().split()))
    for i in range(m):
        a, b = lst[2*i], lst[2*i+1]
        if a>b:
            a, b = b, a
        union(a, b)
    result = []
    for i in range(1, n+1):
        ret = find(i)
        if ret not in result:
            result.append(ret)
    print(f'#{case} {len(result)}')

'''
test case

3
5 2
1 2 3 4
3
5 3
1 2 2 3 4 5
2
7 4
2 3 4 5 4 6 7 4
3
'''