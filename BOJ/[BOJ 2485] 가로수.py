import sys
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]

gaps = [0]*(N-1)
for i in range(1, N):
    gaps[i-1] = trees[i]-trees[i-1]
gaps.sort()

# 1. 최대공약수 구하기
def get_gcd(a, b):
    A, B = max(a, b), min(a, b)
    while (B > 0):
        r = A % B
        A, B = B, r
    return A

common = gaps[0]
for i in range(1, len(gaps)):
    common = get_gcd(common, gaps[i])
n = (trees[-1]-trees[0])//common
print(n-len(trees)+1)


