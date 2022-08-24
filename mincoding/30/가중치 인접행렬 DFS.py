arr = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0]
]

# 재귀를 이용해 구현
# def dfs(now):
#     global value
#     print(now, value)
#     for i in range(6):
#         if arr[now][i]>0 and visited[i]==0:
#             visited[i]=1
#             value += arr[now][i]
#             dfs(i)
# visited=[0]*6
# k = int(input())
# visited[k]=1
# value = 0
# dfs(k)

# 스택을 이용해 구현
def dfs(start_v):
    global total
    stack = [start_v]
    value = [0]*len(arr[0])
    while stack:
        v = stack.pop()
        # print(v, total)
        if v not in used:
            used.append(v)
            print(v, value[v])
            for i in range(len(arr[v])-1, -1, -1):
                if arr[v][i]>0:
                    stack.append(i)
                    value[i]=value[v]+arr[v][i]
    return used
used = []
k=int(input())
dfs(k)




