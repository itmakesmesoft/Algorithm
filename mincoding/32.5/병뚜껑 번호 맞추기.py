n = int(input())
start, end= 1, 50
flag = 1
for i in range(n):
    num, order = input().split()
    num = int(num)
    if order == 'UP':
        start = num+1
    elif order == 'DOWN':
        end = num-1
    if start > end:
        flag = 0 # ERROR
    elif start == end:
        break
if flag:
    if start!=end:
        print(f'{start} ~ {end}')
    else:
        print(f'{start}')
else:
    print('ERROR')


'''
test case
5
15 DOWN
14 DOWN
3 UP
6 UP
10 UP

4
20 UP
23 DOWN
21 UP


3
10 UP
35 DOWN
7 DOWN

'''