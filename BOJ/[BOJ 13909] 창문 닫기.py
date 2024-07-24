N = int(input())
answer = 0
for i in range(1, int(N**(0.5))+1):
    res = i**2
    if res == int(res):
        answer+=1
print(answer)

# 간단 풀이
# N = int(input())
# print(int(N**(0.5)))