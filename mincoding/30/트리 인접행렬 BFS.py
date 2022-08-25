arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

def bfs(start):
    visited=[]
    queue = [start]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            print(v,end = ' ')
            for i in range(len(arr[v])):
                if arr[v][i]>0:
                    queue.append(i)
k = int(input())
bfs(k)
