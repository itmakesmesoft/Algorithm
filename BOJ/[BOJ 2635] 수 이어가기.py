'''
test case
1

100

30000
'''

n = int(input())
max_cnt = 0
path = []
for s in range(n//2, n+1):
    tmp_path = [n]
    f = n
    cnt = 1
    while s >= 0:
        tmp_path.append(s)
        tmp = f-s
        f, s = s, tmp
        cnt += 1
    if max_cnt <= cnt:
        max_cnt = cnt
        path = tmp_path[:] # 얕은 복사 방지
print(max_cnt)
print(*path)