def istrirun(bucket):
    for i in range(8):
        if bucket[i]==3:
            return True
        elif bucket[i] and bucket[i+1] and bucket[i+2]:
            return True
    return False

t = int(input())
for case in range(1, t+1):
    cards = list(map(int, input().split()))
    A = [0]*10
    B = [0]*10
    flag = 0
    while cards:
        A[cards.pop(0)] += 1
        B[cards.pop(0)] += 1
        if istrirun(A):
            flag = 1
            break
        elif istrirun(B):
            flag = 2
            break
    print(f'#{case} {flag}')

'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

4
0 0 0 1 1 1 1 1 1 1 0 1
0 1 0 2 1 2 1 4 2 3 3 3
0 1 0 3 1 2 0 3 2 3 3 1
9 0 8 0 7 5 4 3 2 1 6 4

3
9 0 8 0 7 0 0 2 3 1 2 3 
9 0 9 0 9 0 1 2 3 1 2 3 
8 0 7 0 9 1 1 2 3 1 2 3 


2
0 1 1 3 4 4 3 7 8 8 3 9
0 0 1 0 2 0 1 2 3 2 1 4 
'''


