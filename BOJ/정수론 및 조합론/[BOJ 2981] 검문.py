# 유클리드 호제법
'''
a, b의 최대공약수를 구하는 방법
a, b = b, a%b
'''

# def common_factor(a, b):
#     while b>0:
#         a, b = b, a%b
#     return a

# def is_cf(arr):
#     while len(arr)>1:
#         tmp = []
#         for i in range(len(arr)-1):
#             val = common_factor(arr[i], arr[i+1])
#             if val == 1:
#                 return False
#             tmp.append(val)
#         arr = tmp[:]
#     print(arr)
#     return True

# n = int(input())
# lst = [int(input()) for _ in range(n)]
# print(is_cf(lst))

def getGCF():
    a, b = lst[0], lst[1]
    for i in range(1, len(lst)):
        while b>0:
            a, b = b, a%b
        b = lst[i]
    return a

n = int(input())
lst = [int(input()) for _ in range(n)]
min_lst = min(lst)
result=[]
for i in range(min_lst-1):
    res = getGCF()
    if res != 1 and res not in result:    # 최대공약수가 1 빼곤 없는 경우
        result.append(res)
    for j in range(len(lst)):   # lst 요소를 -1 씩 계산 후 다시 반복
        lst[j]-=1
print(*result)