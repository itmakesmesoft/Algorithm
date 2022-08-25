def abc(start, end):
    if start==end:
        return start
    a = abc(start, (start+end)//2)
    b = abc((start+end)//2+1, end)

    #가위바위보
    if arr[a] - arr[b] == -1 or arr[a] - arr[b] == 2: 
        return b
    else:
        return a

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = abc(0, n-1)+1 # start, end
    print(f'#{case} {result}')

'''
test case
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''