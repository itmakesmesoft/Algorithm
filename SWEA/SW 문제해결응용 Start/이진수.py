def hex2bin(number):
    # 문자 -> 숫자 변환
    if number in ['A','B','C','D','E','F']:
        number = ord(number)-55
    else:
        number = int(number)

    # 이진수 변환 계산
    res = ""
    for _ in range(4):
        res = str(number%2) + res
        number//=2
    return res

T = int(input())
for case in range(1, T+1):
    n, hexa = input().split()
    n = int(n)
    result = ""
    for i in range(n):
        result += hex2bin(hexa[i])
    print(f'#{case} {result}')


'''
3
4 47FE
5 79E12
8 41DA16CD
'''