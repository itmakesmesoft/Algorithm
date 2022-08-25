n = int(input())
arr = list(map(int, input().split()))
result = []
stack = []
while True:
    q = arr.pop(0)
    if len(arr)==0:
        result+stack
        break
    if len(stack)==0:
        stack.append(q)
    else:
        p = stack.pop()
        if p==q:
            stack.append(p)
            stack.append(q)
        else:
            result.append(p)
            stack.append(q)
        if len(stack)>=3:
            stack = []
result.sort()
print(result)
    
    