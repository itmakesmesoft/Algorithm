t = int(input())
for case in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key = lambda x:x[1])
    cnt = 1
    prev = lst[0][1]
    for i in range(1, n):
        if prev<=lst[i][0]:
            prev = lst[i][1]
            cnt+=1
    print(f'#{case} {cnt}')

'''
test case

3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''