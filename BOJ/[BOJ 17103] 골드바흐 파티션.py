import sys
input = sys.stdin.readline

# LinkedList 이용
def find(num, step): # num의 prev 또는 next를 찾는 함수
    global linked
    # linked에 등록되어 있다면 해당 num 값의 prev 또는 next를 이용
    # num이 linked에 없다면 추가
    if not num in linked: linked[num] = [0, 0, 0]
    idx = num+step
    if linked[num][step]==0: # linked의 num의 step번째 인덱스 값이 0인 경우
        while idx>=2 and idx<=N:
            if table[idx]==1:
                linked[num][step]=idx
                break
            idx+=step
        else: linked[num][step]=-1
    return linked[num][step]


# 소수 구하기 -> 에라토스테네스의 체 이용
linked = {} # LinkedList 초기화 -> {...num: [0, prev, next]...} num의 prev, next 인덱스
table = [0, 0] + [1]*999999
for num in range(2, 1002):
    if table[num]==1:
        k = 2
        while num*k<=1000000:
            table[num*k]=0
            k+=1

# 소수의 합 == N 구하기
# 투포인터
T = int(input())
for i in range(T):
    N = int(input())
    left, right = 2, N
    count = 0
    while left<=right:
        if left+right<N:
            left=find(left, 1)
        elif left+right>N:
            right=find(right, -1)
        else: # left+right==N:
            count+=1
            right=find(right, -1)
            left=find(left, 1)
        if right<0 or left<0: break
    print(count)