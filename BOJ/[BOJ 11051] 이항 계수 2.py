import sys
input = sys.stdin.readline
N, K = map(int, input().split())

# 조합
# 메모이제이션
def factorials():
    global memo
    for i in range(1001):
        if i <= 1:
            memo[i] = 1
            continue
        memo[i] = memo[i-1]*i    
        
memo = [0]*1001
factorials()
result = (memo[N]//(memo[N-K]*memo[K]))%10007
print(result)