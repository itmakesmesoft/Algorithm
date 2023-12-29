# 200분

import sys
input = sys.stdin.readline

def get_next(word):
  tmp_word = list(word)
  n = len(tmp_word)
  stack = []
  tmp = ""
  while tmp_word:
    last = tmp_word.pop()
    if stack:
      if last < stack[-1]:
        stack.sort()
        tmp = last
        for i in range(len(stack)):
          if stack[i]>last:
            tmp = stack.pop(i)
            stack.append(last)
            stack.sort()
            break
        return "".join(tmp_word) + tmp + "".join(stack)
      else:
        stack.append(last)
    else:
      stack.append(last)
  return "".join(sorted(stack, reverse=True))


T = int(input())
for _ in range(T):
  word = list(input().rstrip())
  print(get_next(word))
