A, B = map(int, input().split())

# 최대공약수 구하기
# 두 수를 곱한 수를 최대공약수로 나누기
def get_gcd(a, b):
    if b>a: a, b = b, a
    while b>0:
        r = a % b
        a, b = b, r
    return a

common = get_gcd(A, B)
print(A*B//common)
