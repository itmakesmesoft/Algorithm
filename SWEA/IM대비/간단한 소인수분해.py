t = int(input())
for case in range(1, t+1):
    N = int(input())
    arr = [2,3,5,7,11]
    cnt = [0,0,0,0,0]
    for i in range(5):
        while N % arr[i]==0:
            N//=arr[i]
            cnt[i]+=1
    print(f'#{case} {cnt[0]} {cnt[1]} {cnt[2]} {cnt[3]} {cnt[4]}')

'''

10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

'''