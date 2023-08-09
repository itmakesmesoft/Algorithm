import sys
input = sys.stdin.readline

def select(depth):
    global Map, flag
    if flag: return
    if depth==3:
        res = confirm()
        if res: flag = True
        return
    for i in range(N):
        for j in range(N):
            if Map[i][j]=='X':
                Map[i][j]='O'
                select(depth+1)
                Map[i][j]='X'

def confirm():
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    for y, x in Teachers:
        for i in range(4):
            k=1
            while True:
                ny, nx = y+d[i][0]*k, x+d[i][1]*k
                if ny>N-1 or nx>N-1 or ny<0 or nx<0: break
                if Map[ny][nx]=='O': break
                if Map[ny][nx]=='S': return False
                k+=1
    return True


N = int(input())
Map = [list(input().split()) for _ in range(N)]
flag = False

# Map을 순회하며 T인 칸 찾기
Teachers = []
for i in range(N):
    for j in range(N):
        if Map[i][j]=='T':
            Teachers.append((i, j))

select(0)
print('YES' if flag else 'NO')