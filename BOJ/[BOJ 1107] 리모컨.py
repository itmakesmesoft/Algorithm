# 구글 검색 참고함

N = int(input())
M = int(input())
if M: broken = list(input().split())
else: broken = []
answer = abs(100-N)

for num in range(1000001):
    for n in str(num):
        if n in broken: break
    else:
        answer = min(answer, len(str(num)) + abs(num-N))

print(answer)
