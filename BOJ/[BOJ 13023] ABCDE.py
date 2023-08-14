import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def connect(index, cnt):
    global flag, visited
    if cnt>=4:
        flag = True
        return
    if flag: return
    for node in linkedlist[index]:
        if visited[node]==0:
            visited[node]=1
            connect(node, cnt+1)
            visited[node]=0

# 링크드 리스트 이용
linkedlist = [[] for _ in range(N)]

# 링크드 리스트에 연결된 노드 추가
for _ in range(M):
    a, b = map(int, input().split())
    linkedlist[a].append(b)
    linkedlist[b].append(a)

flag = False
for i in range(N):
    if flag: break
    if linkedlist[i] != []:
        visited = [0]*N
        visited[i]=1
        connect(i, 0)

print(1 if flag else 0)