arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']
keywords = input()
cnt = 0
for i in range(6):
    flag = 1
    for j in range(4):
        if keywords[j]=='?': continue
        elif keywords[j]!=arr[i][j]:
            flag = 0
    if flag:
        cnt+=1
print(cnt)