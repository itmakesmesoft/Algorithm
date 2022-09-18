n = int(input()) # 간선의 갯수
lst = [list(input().split()) for _ in range(n)]
arr = [0]*200

def find(x):
    global lst
    if arr[ord(x)] == 0:
        return x
    ret = find(arr[ord(x)])
    arr[ord(x)] = ret
    return ret


def union(a, b):
    global arr
    if find(a)==find(b):
        return True
    arr[ord(b)] = a


flag = 0
for i in range(n):
    a, b = lst[i]
    if union(a, b):
        flag = 1
        break

if flag:
    print("발견")
else:
    print("미발견")


'''
test case
4
A C
A B
B D
C B
'''