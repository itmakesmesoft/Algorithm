import sys
input = sys.stdin.readline

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
schedules.sort(key=lambda x:(x[1], x[0]))

prev = 0
count = 0
for i in range(N):
    start, end = schedules[i]
    if start>=prev:
        count+=1
        prev = end
print(count)

'''
2
1 1
0 1

2
0 1
1 1
'''