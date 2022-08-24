# name = [12,9,3,6]
# arr = [
#    #12 9 3 6
#     [0,1,1,0], # 12
#     [1,0,0,1], # 9
#     [1,0,0,1], # 3
#     [0,1,1,0]  # 6
# ]

# def bfs(start):
#     queue = [start]
#     while queue:
#         v = queue.pop(0)
#         if v not in visited:
#             print(name[v])
#             visited.append(v)
#             for i in range(len(arr[v])):
#                 if arr[v][i]>0:
#                     queue.append(i)
#     return

# k = int(input())
# visited=[]
# k = k//90
# bfs(3)

idx = [0, 1, 3, 2]
arr = [12, 9, 6, 3]
k = int(input())
k //= 90
for _ in range(k):
    arr.append(arr.pop(0))
for i in idx:
    print(arr[i], end = ' ')