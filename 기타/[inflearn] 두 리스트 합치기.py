from collections import deque

res = deque()
n = int(input())
lst1 = list(input().split())
m = int(input())
lst2 = list(input().split())

while lst1 or lst2:
    if lst1 == []:  # lst1의 원소가 없는 경우
        res.appendleft(lst2.pop())
        continue
    if lst2 == []:  # lst2의 원소가 없는 경우
        res.appendleft(lst1.pop())
        continue
    a, b = lst1.pop(), lst2.pop()
    # lst1의 원소가 큰 경우
    if a > b:
        res.appendleft(a)
        lst2.append(b)

    # lst2의 원소가 큰 경우
    elif a < b:
        res.appendleft(b)
        lst1.append(a)

    # 서로 같은 경우
    else:
        res.appendleft(a)
        res.appendleft(b)

print(*res)
