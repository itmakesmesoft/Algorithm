t = int(input())
for case in range(1, t+1):
    cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    bucket = [0]*8
    change = int(input())
    i = 0
    while change and i<8:
        if change >= cash[i]:
            bucket[i]+=(change//cash[i])
            change%=cash[i]
        i+=1
    print(f'#{case}')
    print(*bucket)


'''
2 
32850
160     
'''