'''
test case

4
3 4 1 6
7 7 2 4
2 6 4 5
4 2 6 5
0 1 0 0
0 1 0 0
0 0 1 0
0 1 0 0


6
1 1 1 1 1 1
2 2 2 2 2 2
3 3 3 3 3 3
6 6 6 6 6 6
7 7 7 7 7 7
8 8 8 8 8 8
0 1 1 0 0 0
1 1 0 0 0 0
1 1 0 0 0 0
1 1 0 1 0 0
0 0 0 1 1 1
1 1 0 1 0 0
'''

'''
[정렬 우선 순위]
1. 빈도수가 높을 수록, 우선순위가 높다.
2. 숫자가 작을수록, 우선순위가 높다.
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bitarr = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if bitarr[i][j]==1:
            result.append(arr[i][j])
# DAT
bucket = [0]*10
for i in range(len(result)):
    bucket[result[i]] += 1
# 우선순위대로 나열
while True:
    max_idx = 9
    max_val = 0
    for i in range(9, -1, -1):
        if bucket[i] >= bucket[max_idx]:
            max_idx = i
            max_val = bucket[i]
    for i in range(bucket[max_idx]):
        print(max_idx, end=' ')
    bucket[max_idx] = 0
    if max_val==0:
        break
