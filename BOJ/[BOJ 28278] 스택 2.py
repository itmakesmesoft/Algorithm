import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = list(map(int, input().split()))
    length = len(stack)
    if order[0]==1:
        stack.append(order[1])
    elif order[0]==2:
        print(stack.pop() if length>0 else -1)
    elif order[0]==3:
        print(length)
    elif order[0]==4:
        print(1 if length==0 else 0)
    else:
        print(stack[-1] if length>0 else -1)
