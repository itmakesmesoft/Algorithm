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
    global plate, Max, Max_path
    backup = plate[:]
    if total == n:
        Sum = 0
        tmp = []
        for i in range(n):
            if path[i]==1:
                tmp.append(origin[i])
                Sum += origin[i]
        if Sum > Max:
            Max_path = tmp[:]
            Max = Sum
        return
    for i in range(n):
        if plate[i]==0: continue
        cnt = shoot(i)
        path[i]=1
        dfs(total + cnt)
        path[i]=0
        plate = backup[:]

n = int(input())
plate = list(map(int, input().split()))
origin = plate[:]
Max = -21e8
Max_path = []
path = [0]*n
dfs(0)

while len(Max_path)>1: # 출력
    print(f'{Max_path.pop(0)}+', end='')
print(f'{Max_path.pop(0)}={Max}')


'''
test case
5
3 5 1 7 4
'''