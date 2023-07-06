import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
st, ed = 0, N-1
min_s = int(21e8)
min_lst = []
while st<ed:
    s = lst[st]+lst[ed]
    if abs(s) < min_s:
        min_s = abs(s)
        min_lst = [lst[st], lst[ed]]
    if s >= 0:
        ed-=1
    elif s < 0:
        st+=1
print(*min_lst)