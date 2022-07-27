# n홀수 => s1-s3
#     s2,s3 중에 작은것으로 옮김 => s1-s2
#         s1>s2 and s1>s3
#             s2, s3중에 작은 것 선택, s1, s2중에 작은 것으로 옮김 => s3-s2
#             s1-s3 => len(s1)==0
#         s2-s1
#     s2-s3
# s1-s3

# n = int(input())
# st = [list(range(n+1)), [0], [0]]
# print(st)

# def recursive(st_a, st_b, st_c): #st_a =기준 스택/ st_b,c = 비교 스택
#     if st_a[-1]>st_c[-1] or st_a[-1]>st_b[-1]:
#         if st_a[-1]==n:
#             return st_c.append(st_a.pop())
#         else:
#             if st_b[-1]>st_c[-1]:
#                 st_c.append(st_a.pop())
#                 recursive(st_a, st_b, st_c)
#             else:
#                 st_b.append(st_a.pop())
#                 recursive(st_a, st_b, st_c)
#     else:
#         if st_b[-1]>st_c[-1]:
#             recursive(st_c, st_a, st_b)
#         else:
#             recursive(st_b, st_a, st_c)

# if n%2==0:
#     recursive(n)
# else:
#     pass

# id_number=str(input())
# res=""
# for i, n in enumerate(id_number):
#     if i <= 5:
#         res+=id_number[i]
#     elif i<=12:
#         res+="*"
# print(res)


