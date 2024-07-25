import sys
input = sys.stdin.readline

N = int(input())
waiting = list(map(int, input().split()))
stack = []

number = 1
while waiting:
    if waiting[0]==number:
        number+=1
        waiting.pop(0)
    else:
        if len(stack)>0 and stack[-1]==number:
            stack.pop()
            number+=1
        else:
            stack.append(waiting.pop(0))
while stack:
    if stack[-1]!=number: break
    else:
        stack.pop()
        number+=1
print("Nice" if len(stack)==0 else "Sad")

# 다른 풀이
# N = int(input())
# target = 1
# L = list(map(int, input().split()))
# stack = []
# for i in L:
#     stack.append(i)
#     while stack and stack[-1] == target:
#         stack.pop()
#         target += 1
# if stack:
#     print("Sad")
# else:
#     print("Nice")
