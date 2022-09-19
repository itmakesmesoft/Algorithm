'''
3
0.625
0.1
0.125
'''

T = int(input())
for case in range(1, T+1):
    number = float(input())
    result = ""
    tmp = 0
    flag = 0
    i = 1
    while i<=12:
        val = tmp + 2**(-1*i)
        if number > val:
            tmp = val
            result += "1"
        elif number < val:
            result += "0"
        else:
            result += "1"
            flag = 1
            break
        i+=1
    if flag:
        print(f'#{case} {result}')
    else:
        print(f'#{case} overflow')