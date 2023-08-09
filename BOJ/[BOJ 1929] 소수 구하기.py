M, N = map(int, input().split())
table = [0, 0] + [1]*(N-1)
for i in range(2, int(N**(0.5))+1):
    if table[i]==1:
        j=2
        while i*j<=N:
            table[i*j]=0
            j+=1

for i in range(M, N+1):
    if table[i]==1: print(i)