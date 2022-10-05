n = int(input())
lst = list(map(int, input().split()))
lst.sort()
new_lst = [0]*n
new_lst[0] = lst[0]
for i in range(1, n):
    new_lst[i] = lst[i] + new_lst[i-1]
print(sum(new_lst))

'''
5
3 1 4 3 2
'''
