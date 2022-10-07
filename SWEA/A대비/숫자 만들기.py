def getresult(total, num, index):
    if index==0:
        print("+")
        return total+num
    elif index==1:
        print("-")
        return total-num
    elif index==2:
        print("*")
        return total*num
    else:
        print("/")
        return int(total/num)

def dfs(level, total):
    global max_tot, min_tot, lst
    print(level, total)
    if level==n:
        if max_tot < total:
            max_tot = total
        if min_tot > total:
            min_tot = total
        return
        
    for i in range(4):
        if lst[i] > 0:
            lst[i] -= 1
            tmp = total + getresult(total, number[level], i)
            dfs(level+1, tmp)
            lst[i] += 1

t = int(input())
for case in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    number = list(map(int, input().split()))
    min_tot = 21e8
    max_tot = -21e8
    dfs(1, number[0])
    print(max_tot, min_tot)