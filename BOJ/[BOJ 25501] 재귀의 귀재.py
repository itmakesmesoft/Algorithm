def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def recursion(s, left, right):
    global cnt
    cnt+=1
    if left>=right: return 1
    elif s[left] != s[right]: return 0
    else: return recursion(s, left+1, right-1)
t = int(input())
for case in range(1, t+1):
    s = input()
    cnt = 0
    ret = isPalindrome(s)
    print(ret, cnt)

'''
5
AAA
ABBA
ABABA
ABCA
PALINDROME
'''