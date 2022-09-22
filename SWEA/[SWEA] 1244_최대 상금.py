def getsum(num):
    total = 0
    for i in range(len(num)):
        total+=int(num[i])*10**(len(num)-i-1)
    return total

def recursive(level):
    global num, max_total, max_num, memo
    total = getsum(num)
    if total in memo[level]: return
    memo[level].append(total)
    if level == cnt:
        if total > max_total:
            max_total = total
            max_num = num[:]
        return
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            if getsum(num) not in memo[level]: recursive(level+1)
            num[i], num[j] = num[j], num[i]


t =int(input())
for case in range(1, t+1):
    num, cnt = input().split()
    num, cnt = list(num), int(cnt)
    max_total = -21e8
    memo = [[] for _ in range(cnt+1)]
    max_num = []
    recursive(0)
    print(f'#{case}', end=' ')
    for i in range(len(num)):
        print(max_num[i], end='')
    print()

'''
3
123 1
2737 1
32888 2
'''