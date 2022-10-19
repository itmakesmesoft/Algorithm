S = input()
q = int(input())
lst = [[0]*len(S) for _ in range(26)]
for i in range(len(S)):
    lst[ord(S[i])-97][i]+=1
    
for i in range(len(S)-1):
    for j in range(26):
        lst[j][i+1]+=lst[j][i]
        
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    if l == 0:
        print(lst[ord(a)-97][r])
    else:
        print(lst[ord(a)-97][r]-lst[ord(a)-97][l-1])
    
    
'''
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10

'''