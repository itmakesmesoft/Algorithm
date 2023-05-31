string = input()
flag = True


def divide(substr):
    global flag
    stack = []
    substring = []

    for i in range(len(substr)):
        if substr[i] == '(' or substr[i] == '[':
            stack.append([substr[i], i])
        elif substr[i] == ')' or substr[i] == ']':
            popped, start = stack.pop()
            if (popped == '(' and substr[i] != ')') or (popped == '[' and substr[i] != ']'):
                flag = False
                return
        if stack == []:
            substring.append(substr[start:i+1])
    total = 0
    for sub in substring:
        ln = len(sub)
        if sub == '[]':
            total += 3
        elif sub == '()':
            total += 2
        elif sub[0] == '(':
            total += 2 * divide(sub[1:ln-1])
        else:
            total += 3 * divide(sub[1:ln-1])
    return total


total = divide(string)
if flag:
    print(total)
else:
    print(0)
