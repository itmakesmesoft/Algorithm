import sys
input = sys.stdin.readline

def is_prime(num):
    for i in range(2, len(lst)):
        if lst[i]== False: continue
        if num <= i: return True
        if num % i == 0: return False
    return True

T = int(input())
numbers = [int(input()) for _ in range(T)]
lst = [1]*int(max(numbers)**(0.5)+1)
lst[:2]=[0, 0]
for i, n in enumerate(lst):
    if n==0: continue
    j = 2
    while i * j <= len(lst)-1:
        lst[i*j]=0
        j+=1

for number in numbers:
    k = 0
    if number < 2: print(2)
    else:
        while True:
            if is_prime(number+k):
                print(number+k)
                break
            k+=1
