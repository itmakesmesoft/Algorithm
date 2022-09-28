lst = list(map(int, input().split()))
# 0 2 4 -5 -7 6 20 7 -10 -8  4 -1
def recur(index):
    if index >= 12:
        return 0
    a = lst[index] + recur(index+2)
    b = lst[index] + recur(index+3)
    c = lst[index] + recur(index*2) if index>0 else 0
    return max(a, b, c)
print(recur(0))