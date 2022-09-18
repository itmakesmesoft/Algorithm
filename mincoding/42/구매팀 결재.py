def dfs(level, total):
    global used, Max
    if level == n:
        if total%10 == 0:
            if Max < total:
                Max = total
            return
    for i in range(len(lst)):
        if used[i]==1: continue
        used[i]=1
        dfs(level+1, total - prices[ord(lst[i])-97])
        used[i]=0

prices = [15, 20, 44, 22, 55, 16, 45]
Max = float('-inf')
lst = list(input())
n = int(input())
used = [0]*len(lst)
total = 0
for i in range(len(lst)):
    total += prices[ord(lst[i])-97]
dfs(0, total)
print(Max)