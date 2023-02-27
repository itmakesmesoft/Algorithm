def union(a, b):
    fa, fb = find(a), find(b)
    if fa==fb:
        return True 
    
    return

def find(a):
    global lst
    if lst[a]==a:
        return a
    lst[a]=find(lst[a])
    return lst[a]

N, M = map(int, input().split())
lst = list(range(1, N+1))
cnt = 0
for _ in range(M):
    a, b = map(int,input().split())
    if union(a, b):
        cnt+=1






# import sys
# input = sys.stdin.readline

# def dfs(num):
#     global used
#     for i in range(N):
#         if used[i]==0 and Map[num][i]==1:
#             used[i]=1
#             dfs(i)

# N, M = map(int, input().split())
# Map = [[0]*N for _ in range(N)]
# used = [0]*N
# for _ in range(M):
#     a, b = map(int,input().split())
#     Map[a-1][b-1] = Map[b-1][a-1] = 1

# cnt = 0
# for i in range(N):
#     if used[i]==0:
#         used[i]=1
#         dfs(i)
#         cnt+=1
# print(cnt)