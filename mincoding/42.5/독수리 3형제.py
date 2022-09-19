def getsum(path, level):
    global arr
    s = 0
    for e in range(len(arr)):
        if path[e]>=1:
            s+=(arr[e]*2**(level))
            arr[e]=0
    return s

def dfs(level, total):
    global Max, arr
    backup = arr[:]
    path = [0]*6
    if level == n:
        if total > Max:
            Max = total
        return
    for i in range(0, 3):
        path[i]+=1
        for j in range(3, 6):
            path[j]+=1
            for k in range(1, 5):
                path[k]+=1
                s = getsum(path, level)
                dfs(level+1, total+s)
                arr = backup[:]
                path[k]-=1
            path[j]-=1
        path[i]-=1


arr = list(map(int, input().split()))
n = int(input())
Max = -21e8
dfs(0, 0)
print(Max)

'''

3 7 4 2 6 9
2
'''