n = int(input()) # 노드의 개수
arr = [list(map(int, input().split())) for _ in range(n)]

'''
test case
5
0 0 0 1 0
0 0 1 0 0
0 0 0 1 1
1 0 1 0 1
0 0 1 1 0
'''


def union(a, b): # True: 사이클 발견. False: 미발견
    if find(a)==find(b): # 사이클 발견
        return True
    

def find(x):
    if arr[x]



flag = 0 # 0: 미발견, 1: 발견
for i in range(n-1): # 0, 1, 2, 3, ... n-2
    if union(i, i+1)==True:
        flag = 1

if flag:
    print("cycle 발견")
else:
    print("미발견")