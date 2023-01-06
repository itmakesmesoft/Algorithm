'''
편의상 

1사분면 | 2사분면
ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
3사분면 | 4사분면

으로 가정하고 풀이 진행

'''

N, r, c = map(int, input().split())

def recur(N, r, c):
    global total
    
    if N == 0:
        return
    
    m = 2**(N-1)
    if r < m and c < m:     # 1사분면
        pass
    elif r < m and c >= m:   # 2사분면
        total += (m**2)
    elif r >= m and c < m:   # 3사분면
        total += (m**2 * 2)
    elif r >= m and c >= m:   # 4사분면
        total += (m**2 * 3)
    recur(N-1, r%m, c%m)

total = 0
recur(N, r, c)
print(total)