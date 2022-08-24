t = int(input())
for case in range(1, t+1):
    stack = []
    result = 0
    flag = 0
    arr = list(input().split())
    for i in range(len(arr)):
        if arr[i] == '.':
            break
        elif arr[i] in ['+','-','*','/']:
            if len(stack)<2:
                flag = 0
                break
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if arr[i]=='*':
                    result = val1*val2
                    flag = 1
                elif arr[i]=='/':
                    if val2 == 0: # 숫자를 0으로 나누는 경우 error 출력
                        flag = 0
                        break
                    result = val1//val2
                    flag = 1
                elif arr[i]=='+':
                    result = val1+val2
                    flag = 1
                elif arr[i]=='-':
                    result = val1-val2
                    flag = 1
                stack.append(result)
        else:
            stack.append(int(arr[i])) # 숫자인 경우 스택에 추가
    if flag:
        print(f'#{case} {result}')
    else:
        print(f'#{case} error')

# t = int(input())
 
# for tc in range(1, t+1):
#     arr = list(input().split())
#     stack = []
#     flag = 0
#     for i in arr:
#         if '0' <= i <= '9':
#             stack.append(int(i))
#         elif i == '.':
#             break
#         elif i == '+':
#             if len(stack) < 2:
#                 flag = 1
#                 break
#             stack.append(stack.pop(-2) + stack.pop(-1))
#         elif i == '-':
#             if len(stack) < 2:
#                 flag = 1
#                 break
#             stack.append(stack.pop(-2) - stack.pop(-1))
#         elif i == '*':
#             if len(stack) < 2:
#                 flag = 1
#                 break
#             stack.append(stack.pop(-2) * stack.pop(-1))
#         elif i == '/':
#             if len(stack) < 2:
#                 flag = 1
#                 break
#             stack.append(stack.pop(-2) // stack.pop(-1))
 
#     if flag or len(stack) > 1:
#         print(f'#{tc} error')
#     else:
#         print(f'#{tc} {stack.pop()}')
