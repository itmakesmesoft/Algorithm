t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        v, k = input().split()
        if k not in clothes:
            clothes[k]=1
        else:
            clothes[k]+=1
    total = 1
    for k, v in clothes.items():
        total*=(v+1)
    print(total-1)


'''
test case
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
'''