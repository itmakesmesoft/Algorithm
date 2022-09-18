n = int(input())
plate = list(map(int, input().split()))

def shoot(index):
    global plate
    d = [-1,0,1]
    cnt = 0
    for i in range(3):
        ni = index+d[i]
        if ni>n-1 or ni<0: continue
        if plate[ni]!=0:
            cnt+=1
            plate[ni]=0
    return cnt


def dfs(total):
    global plate
    backup = plate[:]
    if total == n:
        return
    for i in range(n):
        cnt = shoot(i)
        dfs(total + cnt)
        plate = backup[:]

dfs(0)
print()