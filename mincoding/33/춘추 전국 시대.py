populations = [10, 20, 30, 40, 50, 60, 70]
edge = [
    ['alliance', 'A', 'C'],
    ['alliance', 'F', 'C'],
    ['alliance', 'D', 'B'],
    ['alliance', 'A', 'F'],
    ['war', 'D', 'F']
]
arr = [0]*7

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb: return
    arr[ord(fb)-65] = fa

def find(parent):
    if arr[ord(parent)-65] == 0 or arr[ord(parent)-65] == parent:
        arr[ord(parent)-65] = parent
        return parent
    ret = find(arr[ord(parent)-65])
    arr[ord(parent)-65] = ret
    return ret


for i in range(len(edge)):
    a, b = edge[i][1:]
    if edge[i][0]=='alliance':
        if a>b:
            union(b, a)
        else:
            union(a, b)
    else:
        fa, fb = find(a), find(b)
        a_total = b_total = 0
        a_cnt = b_cnt = 0
        for i in range(7):
            if arr[i]==fa:
                a_cnt+=1
                a_total += populations[i]
            elif arr[i]==fb:
                b_cnt+=1
                b_total += populations[i]

if a_total > b_total:
    print(7-b_cnt)
else:
    print(7-a_cnt)