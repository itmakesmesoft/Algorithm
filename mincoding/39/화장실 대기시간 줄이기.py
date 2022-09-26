'''
test case
15 30 50 10
'''
queue = list(map(int, input().split()))
queue.sort()
n = len(queue)
total = 0
for i in range(n-1, -1, -1):
    total += queue[n-i-1]*i
print(total)