t = int(input())
for case in range(1, t+1):
    arr=[10,20,20]
    n = int(input())
    cntarr = [0]*3
    def dfs(cntarr): 
        global cnt
        total = 10*cntarr[0] + 20*(cntarr[1]+cntarr[2])
        if total >= n:
            if total == n:
                cnt+=1
            return
        for i in range(3):
            cntarr[i]+=1
            dfs(cntarr)
            cntarr[i]-=1
    cnt = 0
    dfs(cntarr)
    print(f'#{case} {cnt}')