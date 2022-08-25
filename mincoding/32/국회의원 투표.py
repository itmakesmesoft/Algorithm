'''
test case

5 12
0 sam
1 sammy
3 sole
2 coo
0 luke
1 haily
2 elly
3 hoo
2 kim
2 joon
4 john
4 loo
'''

numbers, citizen = map(int, input().split())
bucket = [0]*numbers
candidates = [[] for _ in range(numbers)]
max_idx = 0
for i in range(citizen):
    num, name = input().split()
    num = int(num)
    candidates[num].append(name)
    bucket[num] += 1
    if bucket[num] > bucket[max_idx]:
        max_idx = num
print(*candidates[max_idx])