def solution(numbers):
    answer = 0
    filt = [1]*(10000000)
    filt[0]=0
    filt[1]=0
    for n in range(2, len(filt)):
        if filt[n]==1:
            i = 2
            while n*i < 10000000:
                filt[n*i]=0
                i+=1

    def dfs(num, level):
        nonlocal memo, used
        if level>len(numbers): return
        if num not in memo and filt[num]==1:
            memo.append(num)
        for i in range(len(numbers)):
            if used[i]==1: continue
            used[i]=1
            dfs(num*10+int(numbers[i]), level+1)
            used[i]=0

    memo = []
    used=[0]*len(numbers)
    dfs(0, 0)
    answer = len(memo)
    return answer