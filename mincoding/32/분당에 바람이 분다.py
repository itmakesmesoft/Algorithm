'''
test case

4
0 0 852
0 2 51
1 1 5
2 0 3
2
4 2
'''

n = int(input())
arr = []
for i in range(n):
    y, x, plants = map(int, input().split())
    arr.append(plants)
k = int(input())
tornados = list(map(int, input().split()))
for j in range(n):
    for i in range(k):
        if arr[j]%10 <= tornados[i]:
            arr[j]=arr[j]//10
            
        else:
            arr[j]-=tornados[i]
total = 0
for j in range(n):
    if arr[j]>0:
        num = arr[j]
        cnt = 0
        while num>0:
            cnt+=1
            num//=10
        total += cnt
print(total)