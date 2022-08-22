'''

3
5
49679
5
08271
10
7797946543

'''

t = int(input())
for case in range(1, t+1):
    n = int(input())
    direct = [0]*10
    number = list(input())
    max_idx = 0
    for i in range(len(number)):
        num = int(number[i])
        direct[num]+=1
    for i in range(10):
        if direct[i]>=direct[max_idx]:
            max_idx = i
    print(f'#{case} {max_idx} {direct[max_idx]}')