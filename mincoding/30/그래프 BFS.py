arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0]
]

def bfs(start):
    queue = [start]
    visited = []
    while queue:
        v = queue.pop(0)
        if v not in visited:
            print(v)
            visited.append(v)
            for i in range(len(arr[v])):
                if arr[v][i]>0:
                    queue.append(i)
start = int(input())
bfs(start)