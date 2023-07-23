lst = input()
number = ''
tmp = 0
total = 0

for i in range(len(lst)-1, -1, -1):
    if lst[i]=="+": # number를 숫자로 변환 후 tmp 값에 더하기
        tmp += int(number)
        number = ''
    elif lst[i]=="-": # tmp에 있는 값에 -씌워서 total에 합하기
        total -= (tmp+int(number))
        number = ''
        tmp = 0
    else: # 현재 number에 넣기
        number = lst[i] + number
total += (tmp + int(number)) # tmp 비우고 total에 더하기
print(total)


# 이전 풀이

# lst = input()
# start = end = 0
# status = 'n' #'y'

# total = 0
# minus = 0 # 음수를 저장할 변수 초기화
# while end < len(lst):
#     if lst[end]=='-':
#         if status == 'y':
#             minus += int(lst[start:end])
#         else:
#             total += int(lst[start:end])
#             status = 'y'
#         start, end = end+1, end+2
#     elif lst[end]=='+':
#         if status == 'y':
#             minus += int(lst[start:end])
#         else:
#             total += int(lst[start:end])
#         start, end = end+1, end+2
#     else:
#         end+=1
# if status == 'y':
#     total -= (minus+int(lst[start:end]))
# else:
#     total += int(lst[start:end])
# print(total)

