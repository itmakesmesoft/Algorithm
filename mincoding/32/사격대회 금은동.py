n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    arr.append([name, score, i])
    arr = sorted(arr, key= lambda x:(x[1], x[2]), reverse=True)[0:3]
    for i in range(len(arr)):
        print(arr[i][0], end=' ')
    print()


'''
test case

5
Hon 90
Da 80
Pro 80
LEM 90
Merry 100
'''
