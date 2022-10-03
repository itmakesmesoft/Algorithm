while True:
    a, b = map(int, input().split())
    if a == 0 and b==0: break
    if a>b:
        if b==1 or a%b==0:
            print('multiple')
        else:
            print('neither')
    elif b>a:
        if a==1 or b%a==0:
            print('factor')
        else:
            print('neither')
