N = int(input())
def hanoi(num, start, to, via):
  global k, lst
  if num==1:
    print(start, to)
    return

  hanoi(num-1, start, via, to)
  print(start, to)
  hanoi(num-1, via, to, start)

print(2**N-1)
if N<21:
  hanoi(N, 1, 3, 2)
