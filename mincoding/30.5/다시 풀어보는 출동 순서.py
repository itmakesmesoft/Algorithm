n = int(input())
arr = ['B', 'I', 'A', 'H']
path = []

i = 0
cnt = 1
while len(path)<4:
    i%=4
    if cnt==n and arr[i] not in path:
        path.append(arr[i])
        print(arr[i], end=' ')
        cnt=1
    if arr[i] not in path: 
        cnt+=1
    i+=1