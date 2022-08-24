n = int(input())
arr = list(map(int, input().split()))
total = 0
for i in range(4):
    total += arr[i]

min_total = total
for i in range(n-4):
    total = total - arr[i] + arr[i+4]
    if total < min_total:
        min_total = total
print(min_total)