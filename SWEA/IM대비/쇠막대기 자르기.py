'''
test case
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''
t = int(input())
for case in range(1, t+1):
    inputs = input()
    n = len(inputs)
    cnt = 0 # 철판의 갯수
    total = 0 # 나눠진 철판의 총 갯수
    for i in range(n):
        if inputs[i]==')':
            if inputs[i-1]=='(': # 레이저인 경우
                cnt -= 1
                total += cnt
            else: # 철판이 끝난 경우
                cnt -= 1
                total += 1
        else: # 철판이 하나 추가
            cnt += 1
    print(f'#{case} {total}')


# 방법 2 스택이용
# for case in range(1, t+1):
#     tc = input()
#     stack = []
#     cnt = 0
#     for i in range(len(tc)):
#         if tc[i] == '(':
#             stack.append('(')
#         else:
#             if tc[i-1] == '(':
#                 stack.pop()
#                 cnt += len(stack)
#             else:
#                 stack.pop()
#                 count += 1
#     print(f'#{test_case} {count}')
            