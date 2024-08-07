# 기약분수 만들기 => 분모와 분자의 최대공약수를 구하고, 각각 최대공약수로 나누기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

parent = a[1]*b[1]
son = a[0]*b[1] + b[0]*a[1]

def get_gcd(A, B):
    if A<B: A, B = B, A
    while B>0:
        r = A % B
        A, B = B, r
    return A

common = get_gcd(parent, son)
print(son//common, parent//common)