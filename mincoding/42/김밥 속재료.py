# 중복 조합
def dfs(level, start):
    global basket
    if level == 3:
        for i in range(3):
            print(basket[i], end='')
        print()
        return
    for i in range(start, len(ingredients)):
        basket[level] = ingredients[i]
        dfs(level+1, i)
        basket[level] = 0

ingredients = list(input())
basket = [0]*3
dfs(0, 0)