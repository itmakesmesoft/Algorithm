t = int(input())
for case in range(1, t+1):
    n, m = map(int,input().split())
    loads = list(map(int, input().split())) 
    cargos = list(map(int, input().split()))
    loads.sort(reverse=True)
    cargos.sort(reverse=True)
    total_weight = 0
    j = -1
    for i in range(m):
        while j<n-1:
            j+=1
            if cargos[i]>=loads[j]:
                total_weight += loads[j]
                break
    print(f'#{case} {total_weight}')



'''
test case

3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''