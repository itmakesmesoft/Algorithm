N = int(input())
lst = list(map(int, input().split()))
stack = []
result = []
for i in range(N-1, -1, -1):
  while stack:
    if lst[i]<stack[-1]:
      result.append(stack[-1])
      break
    else:
      stack.pop()
  if stack==[]:
    result.append(-1)
  stack.append(lst[i])
result.reverse()
print(*result)