lst = input()
start = end = 0
status = 'n' #'y'

total = 0
minus = 0 # 음수를 저장할 변수 초기화
while end < len(lst):
    if lst[end]=='-':
        if status == 'y':
            minus += int(lst[start:end])
        else:
            total += int(lst[start:end])
            status = 'y'
        start, end = end+1, end+2
    elif lst[end]=='+':
        if status == 'y':
            minus += int(lst[start:end])
        else:
            total += int(lst[start:end])
        start, end = end+1, end+2
    else:
        end+=1
if status == 'y':
    total -= (minus+int(lst[start:end]))
else:
    total += int(lst[start:end])
print(total)

