import sys
input = sys.stdin.readline
a, b, c = map(int , input().split())
def recur(k):
  if k==1: return a%c
  res = recur(k//2)
  if k%2==0:
    return (res*res)%c
  else:
    return (a*res*res)%c

print(recur(b))