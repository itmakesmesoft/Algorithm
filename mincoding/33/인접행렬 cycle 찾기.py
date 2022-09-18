'''
test case

5
0 0 0 1 0
0 0 1 0 0
0 0 0 1 1
1 0 1 0 1
0 0 1 1 0
'''


def find(parent):
    if arr[ord(parent)]==0:
        return parent
    ret = find(arr[ord(parent)])
    arr[ord(parent)] = ret  # 경로 압축
    return ret


def union(a, b):
    if find(a)==find(b): 
        return True
    arr[ord(b)] = a
    return False


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

edge = []

for i in range(n): # 간선 정보 생성
    for j in range(i, n):
        if lst[i][j]==1:
            edge.append([chr(i+65), chr(j+65)])

# Union-find로 사이클 여부 확인
flag = 0
arr = [0]*200
for i in range(len(edge)):
    a, b = edge[i]
    if union(a, b):
        flag = 1 # 1: 사이클 존재 | 0: 존재하지 않음
        break
if flag:
    print("cycle 발견")
else:
    print("미발견")