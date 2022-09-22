from collections import deque

def control(curr, index):
    if index==0:
        next_channel = curr//2
    elif index==1:
        next_channel = curr*2
    elif index==2:
        next_channel = curr+1
    elif index==3:
        next_channel = curr-1
    return next_channel

def bfs(curr):
    global used
    q = deque()
    q.append([curr, 0])

    while q:
        curr, cnt = q.popleft()
        if curr==goal:
            break
        for i in range(4):
            next_channel = control(curr, i)
            if next_channel > 100000 or next_channel<0: continue
            if used[next_channel]==1: continue
            used[next_channel]=1
            q.append([next_channel, cnt+1])
    return cnt

curr = int(input())
goal = int(input())
used = [0]*100001
print(bfs(curr))