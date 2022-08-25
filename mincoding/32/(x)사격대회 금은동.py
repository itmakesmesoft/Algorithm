n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    arr.append([name, score])
    arr = sorted(arr, key= lambda x:x[1], reverse=True)
    for i in range(len(arr)):
        if i==3:
            break
        else:
            print(arr[i][0], end=' ')
    print()


'''
5
Hon 90
Da 80
Pro 80
LEM 90
Merry 100
'''