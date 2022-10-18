# def dfs(level):
#     global cnt
#     print(level)
#     if level==n:
#         cnt+=1
#         return
#     for i in range(n):
#         for j in range(n):
#             if lr[i+j]==0 and rl[n-j+i-1]==0 and row[i]==0 and col[j]==0:
#                 lr[i+j] = rl[n-j+i-1] = row[i] = col[j] = 1
#                 dfs(level+1)
#                 lr[i+j] = rl[n-j+i-1] = row[i] = col[j] = 0


# t = int(input())
# for case in range(1, t+1):
#     n = int(input())
#     Map = [[0]*n for _ in range(n)]
#     row = [0]*n
#     col = [0]*n
#     lr = [0]*2*n
#     rl = [0]*2*n
#     cnt= 0 
#     dfs(0)
#     print(cnt)
    