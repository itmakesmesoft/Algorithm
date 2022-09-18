def union(a, b):
    fa, fb = find(a), find(b)
    if fb.isalpha():
        fb = b
    
    arr[b] = fa

def find(parent):
    if parent.isalpha() or parent==0: # 등급 또는 0인 경우
        return parent
    ret = find(arr[parent]) # 품목 번호인 경우
    arr[parent] = ret
    return ret





N, K = map(int, input().split())
edge = [list(input().split()) for _ in range(N)]
arr = [0]*K

for i in range(N):
    a, b = edge[i]
    union(a, b)


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