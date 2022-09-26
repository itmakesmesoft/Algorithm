'''
test case

8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''

def dfs(now):
    if now > n:
        return
    dfs(now*2)
    print(edge[now], end='')
    dfs(now*2+1)

for case in range(1, 11):
    n = int(input())
    edge = [0]*(n+1)
    for i in range(n):
        lst = input().split()
        edge[int(lst[0])] = lst[1]
    print(f'#{case}', end=' ')
    dfs(1)
    print()




# def dfs(now):
#     if edge[now]==0: return
#     if edge[now]:
#         val = edge[now].pop(0)
#         dfs(val)
#         print(lst[i], end='')



# for case in range(0, 1):
#     n = int(input())
#     edge = [0]*(n+1)
#     lst = [0]*(n+1)
#     for i in range(1, n+1): # 간선배열 채우기
#         edge_info = list(input().split())
#         num, alpha = int(edge_info[0]), edge_info[1]
#         lst[i]=alpha
#         if len(edge_info)==4:
#             first, second = int(edge_info[2]), int(edge_info[3])
#             edge[num] = [first, second]
#         elif len(edge_info)==3:
#             first = int(edge_info[2])
#             edge[num] = [first]
#     print(edge)
#     dfs(1)
#     print(lst)


# def inorder(n):
#     global N
#     if n > N: return
#     inorder(2*n)
#     print(arr[n], end='')
#     inorder(2*n+1)

# for case in range(1, 11):
#     N = int(input())
#     arr = [0]*(N+1)
#     for i in range(N):
#         tmp = list(input().split())
#         arr[int(tmp[0])]=tmp[1]
#     print(f'#{case}', end=' ')
#     inorder(1)
#     print()




