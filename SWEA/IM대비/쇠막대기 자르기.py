'''
() = 레이저
( = 쇠막대기
'''
t = int(input())
for case in range(1, t+1):
    tc = input()
    stack = []
    cnt = 0
    for i in range(len(tc)):
        if tc[i] == '(':
            stack.append('(')
        else:
            if tc[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            