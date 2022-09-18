arr = [0,'A','A','E',0,'E',0,'G',0,'I']
n = int(input())
lst = [list(input().split()) for _ in range(n)]


def find(x):
    if arr[ord(x)-65]==0: return x
    ret = find(arr[ord(x)-65])
    arr[ord(x)-65] = ret
    return ret

def union(a,b):
    if find(a) == find(b): return
    arr[ord(b)-65]=a

for i in range(n):
    a, b = lst[i]
    union(a, b)

cnt = 0
for i in range(len(arr)):
    if arr[i]==0:
        cnt+=1
print(f'{cnt}개')

'''
test case
3
G I
D E
H J
'''