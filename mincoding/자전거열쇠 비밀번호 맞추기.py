def dfs(level):
    global cnt, flag
    if level == 4:
        if ''.join(path) == password:
            flag = 1
        cnt+=1
        return
    for i in range(65, 91):
        if flag==0:
            path[level]=chr(i)
            dfs(level+1)
            path[level]=''

t = int(input())
for _ in range(t):
    cnt = flag = 0
    path = ['']*4
    password = input()
    dfs(0)
    print(cnt)