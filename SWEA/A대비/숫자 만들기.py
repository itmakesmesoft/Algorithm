def dfs(level, total):
    global max_total, min_total
    if level==n:
        if total > max_total:
            max_total = total
        if total < min_total:
            min_total = total
        return
    for i in range(4):
        if canuse[i]>0:
            canuse[i]-=1
            tmp = total
            if i==0:
                tmp+=numbers[level]
            elif i==1:
                tmp-=numbers[level]
            elif i==2:
                tmp*=numbers[level]
            else:
                tmp=int(tmp/numbers[level])
            dfs(level+1, tmp)
            canuse[i]+=1
    
t = int(input())
for case in range(1, t+1):
    n = int(input())
    canuse = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_total = -21e8
    min_total = 21e8
    dfs(1, numbers[0])
    print(f'#{case} {max_total-min_total}')
    
'''
10
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6 
5
1 1 1 1
9 9 9 9 9 
6
1 4 0 0
1 2 3 4 5 6 
4
0 2 1 0
1 9 8 6
6
2 1 1 1
7 4 4 1 9 3 
7
1 4 1 0
2 1 6 7 6 5 8 
8
1 1 3 2
9 2 5 3 4 9 5 6 
10
1 1 5 2
8 5 6 8 9 2 6 4 3 2 
12
2 1 6 2
2 3 7 9 4 5 1 9 2 5 6 4 
'''