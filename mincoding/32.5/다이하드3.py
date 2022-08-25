def abc(level):
    if arr[level]==0:
        print(f'{level}번')
        return
    abc(level+arr[level])
    print(f'{level}번')

n = int(input())
arr = [3,2,-1,3,-2,0,-1]
abc(n)