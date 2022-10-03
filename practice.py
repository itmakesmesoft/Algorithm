# def dfs(depth, total):
#     global min_total
#     if total > min_total:  return
#     if depth == n:
#         if total < min_total:
#             min_total = total
#         return

#     for i in range(n):
#         if used[i]==1: continue
#         used[i]=1
#         dfs(depth+1, total + lst[depth][i])
#         used[i]=0
        
# t = int(input())
# for case in range(1, t+1):
#     n = int(input())
#     lst = [list(map(int, input().split())) for _ in range(n)]
#     used = [0]*n
#     min_total = 21e8
#     dfs(0, 0)
#     print(f'#{case} {min_total}')

def dfs(now, cnt):
    global min_cnt, memo
    if cnt > min_cnt: return
    if now==n-1:
        if cnt<min_cnt:
            min_cnt = cnt
        return
    if cnt < memo[now]: 
        memo[now]=cnt
    if now+stops[now]>n-1: end = n-now
    else: end = stops[now]+1
    for i in range(1, end):
        if cnt+1 < memo[now+i]: 
            dfs(now+i, cnt+1)
        

t = int(input())
for case in range(1, t+1):
    stops = list(map(int, input().split()))
    n, stops = stops[0], stops[1:]+[0]
    min_cnt = 21e8
    inf = 21e8
    memo = [inf]*n
    dfs(0, 0)
    print(f'#{case} {min_cnt-1}')



'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''