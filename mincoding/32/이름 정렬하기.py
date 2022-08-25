'''
test case

5
aaleh
amily
acome
john
java
'''

n = int(input())
contacts = [input() for _ in range(n)]
for i in range(n):
    for j in range(i, 0, -1):
        if len(contacts[j]) < len(contacts[j-1]):
            contacts[j], contacts[j-1] = contacts[j-1], contacts[j]
        elif len(contacts[j]) == len(contacts[j-1]):
            if contacts[j] < contacts[j-1]:
                contacts[j], contacts[j-1] = contacts[j-1], contacts[j]
for i in range(n):
    print(contacts[i])