# 70분

import sys
input = sys.stdin.readline

def is_same(bucket):
  if bucket != bucket_t: return False
  return True

def manipulate_word(bucket):
  new_bucket = bucket[:]
  for i in range(26):
    if new_bucket[i]>bucket_t[i]:
      new_bucket[i]-=1
      return new_bucket
    elif new_bucket[i]<bucket_t[i]:
      new_bucket[i]+=1
      return new_bucket
  return new_bucket

def change_word(bucket):
  new_bucket = bucket[:]
  change = [0, 0]
  for i in range(26):
    if new_bucket[i]==bucket_t[i]: continue
    if change[0]==0 and new_bucket[i]>bucket_t[i]:
      new_bucket[i]-=1
      change[0]+=1
    elif change[1]==0 and new_bucket[i]<bucket_t[i]:
      new_bucket[i]+=1
      change[1]+=1
  return new_bucket

N = int(input())
target = input().rstrip()
bucket_t = [0]*26
for t in target: bucket_t[ord(t)-65]+=1
lst = [input().rstrip() for _ in range(N-1)]
count = 0
for word in lst:
  bucket = [0]*26
  for w in word: bucket[ord(w)-65]+=1
  if is_same(bucket): count +=1
  elif is_same(manipulate_word(bucket)): count += 1
  elif is_same(change_word(bucket)): count += 1
print(count)



'''
1. 같은 구성인 경우
2. 한 단어에서 한 문자를 더하거나 빼면 같은 경우
3. 하나의 문자를 다른 문자로 바꾸면 같은 경우
'''