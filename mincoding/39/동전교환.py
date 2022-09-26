rest = int(input())
coins = [500, 100, 50, 10]
coin = 0
for i in range(4):
    coin += rest//coins[i]
    rest%=coins[i]
    if rest == 0: break
print(coin)