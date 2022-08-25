string = list(input())
print(''.join(string))
while True:
    for i in range(len(string)):
        if string[i] == '_':continue
        string[i] = chr(ord(string[i])-1)
        if ord(string[i]) < 65:
            string[i] = '_'
    print(''.join(string))
    if string == ['_']*len(string):
        break