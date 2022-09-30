n = int(input())
lst = list(map(int, input().split()))
lst.sort()
new_lst = [0]*n
for i in range(n):
    new_lst = lst[i] + lst[i-1]

1 2 3 3 4
1 3 6 9