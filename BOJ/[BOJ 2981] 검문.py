def GCF(a, b):
    while b>0:
        a, b = b, a%b
    return a

def divisor(number):
    result = [number]
    for i in range(2, int(number**(0.5))+1):
        if number%i==0:
            result.append(i)
            if i != number//i:
                result.append(number//i)
    result.sort()
    return result


n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
arr = [0]*(n-1)
for i in range(n-1):
    arr[i] = lst[i]-lst[i+1]
gcd = arr[0]
for i in range(1, len(arr)):
    gcd = GCF(gcd, arr[i])
result = divisor(gcd)
print(*result)

'''
test case

3
6
34
38


5
5
17
23
14
83
'''