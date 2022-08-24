arr = list(input() for _ in range(3))
# 길이로 순위 필터링
res = []
max_len = 0
for i in range(3):
    arr_len = len(arr[i])
    if arr_len>max_len:
        max_len = arr_len
        res = [arr[i]]
    elif arr_len==max_len:
        res.append(arr[i])

# 같은 길이의 2진수가 2개 이상 남았을 경우 가정
# 앞글자부터 하나씩 pop(0)해서 모두 같은 경우 pass
# 다른 경우 대소 비교
j = 0
while len(res)>1:
    max_val = 0
    tmp = []
    for i in range(len(res)):
        arr_val = int(res[i][j])
        if arr_val>max_val:
            max_val = arr_val
            tmp = [res[i]]
        elif arr_val==max_val:
            tmp.append(res[i])
    res = tmp
    j+=1
print(*res)