from collections import deque

def bfs(num, goal):
    global table
    q = deque()
    q.append([num, 0]) # num, cnt
    while q:
        num, cnt = q.popleft()
        if num == goal: break
        for i in range(4):
            if i==0:
                res = num+1
            elif i==1:
                res = num-1
            elif i==2:
                res = num*2
            elif i==3:
                res = num-10
            if res>1000000 or res<0: continue

            if table[res] > cnt+1:
                table[res] = cnt+1
                q.append([res, cnt+1])
    return 


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    inf = int(21e8)
    table = [inf]*1000001
    cnt = bfs(n, m)
    print(f'#{case} {table[m]}')

'''
test case
3
2 7
3 15
36 1007


3
1 2
2 1
3 1000000
'''