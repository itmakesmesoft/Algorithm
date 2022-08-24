fees = [1,2,3,3,5,1,0,1,3]
m = int(input())
total = 0
for i in range(m): # 초기 합 구하기
    total += fees[i]
min_total = total
for i in range(9-m):
    total = total - fees[i] + fees[i+3]
    if total < min_total:
        min_total = total
print(min_total)