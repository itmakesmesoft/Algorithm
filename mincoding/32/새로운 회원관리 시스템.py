'''
test case

5
redeye
apple
Steve
Berry
eUnBo
'''

n = int(input())
arr = []
for _ in range(n):
    # 첫 글자 소문자
    # 1. 모두 소문자인 경우 => 첫 글자 대문자 + 나머지 소문자로
    # 2. 대 소문자가 뒤섞인 경우=> 모두 대문자로
    
    name = input()
    flag = 1 # 1번 상황
    for i in range(1, len(name)):
        if ord(name[i]) <= 90:
            flag = 2 # 2번 상황
            break
    if flag==1:
        name = name.capitalize()
    else:
        name = name.upper()
    arr.append(name)

#삽입 정렬
for i in range(n):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
for i in range(n):
    print(arr[i])




    