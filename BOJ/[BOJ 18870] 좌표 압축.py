def bs(num):
    start, end = 0, len(sorted_lst)-1
    while start<=end:
        mid = (start+end)//2
        if sorted_lst[mid] == num:             
            return mid
        elif sorted_lst[mid] > num:
            end-=1
        elif sorted_lst[mid] < num:
            start+=1

n = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)
for i in range(n):
    print(bs(lst[i]), end=' ')


'''testcase
5
2 4 -10 4 -9
'''