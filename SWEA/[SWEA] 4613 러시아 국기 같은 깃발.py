# def getcnt(level, start, end):
#     cnt = 0
#     if level == 0:
#         word = 'W'
#     elif level == 1:
#         word = 'B'
#     else:
#         word = 'R'
#     for i in range(start, end):
#         for j in range(m):
#             if lst[i][j]!=word:
#                 cnt+=1
#     return cnt



# def dfs(level, start, cnt):
#     global min_cnt,path
#     if level == 3:
#         cnt += getcnt(level, start, n)
#         if cnt < min_cnt:
#             print(path)
#             min_cnt = cnt
#         return

#     for i in range(start, n):
#         path.append(i)
#         dfs(level+1, i+1, cnt+getcnt(level, i, i+1))
#         path.pop()

# t = int(input())
# for case in range(1, t+1):
#     n, m = map(int, input().split())
#     lst = [list(input()) for _ in range(n)]
#     path = []
#     min_cnt = 21e8
#     dfs(0, 0, 0)
#     print(min_cnt)






def getcnt(path):
    cnt = 0
    c_path = path[:]+[n]
    for k in range(3):
        start, end = c_path[k], c_path[k+1]
        print(start, end)
        if k == 0:
            word = 'W'
        elif k == 1:
            word = 'B'
        else:
            word = 'R'
        for i in range(start, end):
            for j in range(m):
                if lst[i][j]!=word:
                    cnt+=1
    return cnt



def dfs(level, start):
    global min_cnt,path
    if level == 2:
        cnt = getcnt(path)
        print(cnt, path)
        if cnt < min_cnt:
            min_cnt = cnt
        return

    for i in range(start, n):
        path.append(i)
        dfs(level+1, i+1)
        path.pop()


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    path = []
    min_cnt = 21e8
    dfs(0, 0)
    print(min_cnt)

'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW


1
4 5
WRWRW
BWRWB
WRWRW
RWBWR
'''
