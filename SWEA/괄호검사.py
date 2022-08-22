t= int(input())
for case in range(1, t+1):
    string = list(input())
    stack =[]
    while string:
        s = string.pop()
        if s==')' or s=='}':
            stack.append(s)
        else:
            if s == '(':
                if len(stack)>0 and stack[-1]==')':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == '{':
                if len(stack)>0 and stack[-1]=='}':
                    stack.pop()
                else:
                    stack.append(s)
    print(stack)
    if len(stack)==0:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')