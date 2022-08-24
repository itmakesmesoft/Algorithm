t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    pizzas = list(map(int, input().split()))

    queue = pizzas[:n] # 화덕에 올라간 피자들
    pizzas = pizzas[n:] # 남은 피자들
    curr = list(range(1, n+1)) # 화덕에 올라간 피자 번호
    rest = list(range(n+1, m+1)) # 남은 피자 번호

    while len(queue)>1:
        pizza = queue.pop(0)//2
        number = curr.pop(0)
        if pizza > 0:
            queue.append(pizza)
            curr.append(number)
        else:
            if len(pizzas)>0:
                queue.append(pizzas.pop(0))
                curr.append(rest.pop(0))
    print(f'#{case} {curr.pop()}')


''''
test case

3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

'''