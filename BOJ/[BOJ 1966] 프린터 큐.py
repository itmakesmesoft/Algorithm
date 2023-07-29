import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    importances = sorted(lst)
    count = 0

    while lst:
        current, maximum = lst.pop(0), importances[-1]
        if maximum <= current:
            count += 1
            importances.pop()
            if M == 0: break
        else:
            lst.append(current)
        M -= 1
        if M<0: M=len(lst)-1
    print(count)

'''
6 1
1 1 3 4 1 5
=> 6

6 0
1 1 3 4 1 5
=> 5

6 0
1 1 9 1 1 1
=> 5

6 2
1 2 2 2 2 5
=> 3

4 0
1 1 1 1
=> 1

6 5
2 2 1 1 2 2
=> 4

6 5
1 1 1 1 1 1
=> 6

6 5
4 3 2 4 2 1
=> 6

6 0
4 3 3 4 3 3
=> 1
'''
