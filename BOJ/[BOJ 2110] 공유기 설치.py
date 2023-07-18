import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
# Distance를 결정 -> 파라메트릭 서치 이용
max_distance = 0

def parametric_search():
    global max_distance
    start, end = 0, lst[N-1]
    while start<=end:
        mid = (start+end)//2
        if is_possible(mid):
            start = mid + 1
            max_distance = mid
        else:
            end = mid - 1

# 공유기 C개 설치 가능한지 확인
def is_possible(dist):
    last = lst[0]
    cnt = 1
    for i in range(1, N):
        if lst[i]-last>=dist:
            cnt+=1
            last = lst[i]
    return cnt>=C

parametric_search()
print(max_distance)