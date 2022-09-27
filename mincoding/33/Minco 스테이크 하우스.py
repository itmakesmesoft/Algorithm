def find(node):
    global lst
    print(node)
    if node in alphabet:
        return node
    elif lst[node]==node:
        return node
    ret = find(lst[node])
    lst[node]=ret
    return ret


def union(a, b):
    global lst
    if a in alphabet or b in alphabet:
        if a.isalpha():
            b=int(b)
            lst[b]=a
        else:
            a=int(a)
            lst[a]=b
    else:
        a, b=int(a), int(b)
        if a>b:
            a, b = b, a
    fa, fb = find(a), find(b)
    if fa==fb: return
    if fb in alphabet:
        lst[fa]=fb
    else:
        lst[fb]=int(fa)
    return

N, K = map(int, input().split())
edge = [list(input().split()) for _ in range(N)]
lst = list(range(K+1))
alphabet = ['A','B','C','D','E','F']
for i in range(N):
    a, b = edge[i]
    union(a, b)
for i in range(1, K+1):
    print(lst[i],end='')

'''
test case

6 4
3 2
B 4
1 A
3 4
3 B
A 1
'''