import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x:x[0], reverse=True) # 내림차순
    min_b = N+1 # 석차 항상 더 크게 초기화
    count = 0
    while lst:
        a, b = lst.pop() # a: 서류성적, b:면접 성적
        if min_b > b: min_b = b
        else: continue
        count+=1
    print(count)