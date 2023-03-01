def reverse_word(word):
  lst = list(word)
  k = len(lst)
  for i in range(k//2):
    lst[i], lst[k-i-1] = lst[k-i-1], lst[i]
  return ''.join(lst)

lst = input()
start = 0
status = 'closed'

for i in range(len(lst)):
  w = lst[i]
  if w=='<' and status == 'closed':
    print(reverse_word(lst[start:i]), end='')
    start = i
    status = 'open'
  elif w=='>' and status == 'open':
    print(lst[start:i+1], end='')
    start = i+1
    status = 'closed'
  elif w==' ' and status == 'closed':
    print(reverse_word(lst[start:i]), end=' ')
    start = i+1
  elif i==len(lst)-1 and status=='closed':
    print(reverse_word(lst[start:i+1]), end='')