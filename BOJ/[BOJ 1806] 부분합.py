N, S = map(int, input().split())
lst = list(map(int, input().split()))

# 누적합 구하기
Sum = [lst[0]] + [0]*(N-1)
for i in range(1, N):
    Sum[i]=lst[i]+Sum[i-1]

# 투포인터
st, ed = 0, 0
min_length = int(20e8)
flag = False
while ed>=st and ed<N:
    s = Sum[ed]-Sum[st-1] if st>0 else Sum[ed]
    if s>=S:
        flag = True
        length = ed-st+1
        if length < min_length: min_length = length
        st+=1
    else:
        ed+=1

print(min_length if flag else 0)
