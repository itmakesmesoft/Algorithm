from collections import deque

def solution(maps):
    # 모든 통로는 여러 번 지나갈 수 있음
    # 시작, 출구, 레버는 항상 다른곳에 존재, 항상 하나씩 존재

    def bfs(start_y, start_x, target_y, target_x):
        print(start_y, start_x, target_y, target_x)
        q = deque()
        q.append([start_y, start_x, 0]) # start_y, start_x, cnt
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = [[0]*m for _ in range(n)]
        
        while q:
            y, x, cnt = q.popleft()
            if y==target_y and x==target_x:
                
                return cnt
            for i in range(4):
                ny, nx = y+d[i][0], x+d[i][1]
                if ny>n-1 or nx>m-1 or ny<0 or nx<0: continue
                if visited[ny][nx] == 1: continue
                if maps[ny][nx] == 'X': continue
                visited[ny][nx]=1
                q.append([ny, nx, cnt+1])
        return -1
                
    # 레버와 출구 찾고, 배열에 입력
    targets = [[0,0],[0,0],[0,0]] # 0:시작 위치, 1: 레버 위치, 2: 출구 위치
    n=len(maps)
    m=len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                targets[0] = [i, j]
            elif maps[i][j]=='L':
                targets[1] = [i, j]
            elif maps[i][j]=='E':
                targets[2] = [i, j]
                
    # 레버로 이동
    answer = -1
    goto_lever = goto_exit = 0
    
    goto_lever = bfs(targets[0][0], targets[0][1], targets[1][0], targets[1][1])
    if goto_lever > 0: # 레버를 찾은 경우 => exit로 이동
        goto_exit = bfs(targets[1][0], targets[1][1], targets[2][0], targets[2][1])
        if goto_exit > 0:# 결과 반환
            answer = goto_lever + goto_exit
    return answer