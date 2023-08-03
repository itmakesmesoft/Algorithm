N = int(input())

# 아레토스테네스의 체
bucket= [1]*(N+1)
for i in range(2, int(N**(0.5))+1):
    if bucket[i]==1:
        j = 2
        num = i*j
        while num<=N:
            bucket[num]=0
            j+=1
            num = i*j

# 소수의 누적합 구하기
total = 0
lst = [] # 소수의 누적합을 담을 리스트
for num in range(2, len(bucket)):
    if bucket[num]==1:
        total += num
        lst.append(total)

# 투포인터
left = right = total = count = 0
while right<len(lst):
    if left>0:
        total = lst[right]-lst[left-1]
    else: total = lst[right]
    if total > N:
        left+=1
    elif total < N:
        right+=1
    else: # total == N:
        count+=1
        left+=1
        right+=1
print(count)