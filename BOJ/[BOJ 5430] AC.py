import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    P = input().strip()
    N = int(input())
    left, right = 0, N-1
    lst = list(map(str, input().strip("[]\n").split(',')))
    lst = list(map(int, lst)) if lst != [''] else []
    is_reversed = False
    bucket = [1]*N
    flag = False
    for p in P:
        if p=='R':
            is_reversed = False if is_reversed else True
        else:
            if right<left or lst==[]:
                flag = True
                break
            elif is_reversed:
                bucket[right]=0
                right-=1
            else:
                bucket[left]=0
                left+=1

    result = []
    if flag: print('error')
    else:
        for i in range(N):
            if bucket[i]==1:
                result.append(lst[i])
        if is_reversed: result.reverse()
        print('[', end='')
        print(*result, sep=',', end='')
        print(']')