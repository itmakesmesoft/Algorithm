# # def revenue(y, x):
# #     k = 1
# #     while True:
# #         if (2*k-1)>N: break
# #         ny = y-k+1 # y의 시작점
# #         nx = x-k+1 # x의 시작점
# #         mid = k-1
# #         for i in range(2*k-1):
# #             for j in range(2*k-1):
# #                 if ny+i>N-1 or nx+j>N-1 or ny+i<0 or nx+j<0: continue
# #                 if i<=mid:
# #                     if abs(mid-i)<=j and j<=abs(mid+i):
# #                         print(ny+i, nx+j, end=' ')
                
# #                 else:
# #                     if abs(mid-i)<=j and j<2*k-i:
# #                         print(ny+i, nx+j, end=' ')
# #             print()
# #         print()
# #         k+=1




# # t = int(input())
# # for case in range(1, t+1):
# #     N, M = map(int, input().split())
# #     arr = [list(map(int,input().split())) for _ in range(N)]
# #     # for i in range(n):
# #     #     for j in range(n):
# #     #         revenue(i, j)
# #     revenue(2,2)

# '''
# 0: 0 1 2 3 4
# 1: 0 1 2 3 4
# 2: 0 1 2 3 4
# 3: 0 1 2 3 4
# 4: 0 1 2 3 4

# 10
# 8 3
# 0 0 0 0 0 1 0 0
# 0 1 0 1 0 0 0 1
# 0 0 0 0 0 0 0 0
# 0 0 0 1 0 1 0 0
# 0 0 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 1 0
# 1 0 0 0 0 0 0 0
# '''
# t = int(input())
# for case in range(1, t+1):
#     n, m = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(n)]
    