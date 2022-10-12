def getsum(path):
    Range = [0, path[0], path[1], n]
    word = ['W', 'B', 'R']
    cnt = 0
    for k in range(3):
        start, end = Range[k], Range[k+1]
        for i in range(start, end):
            for j in range(m):
                if lst[i][j]!=word[k]:
                    cnt+=1
    return cnt

def dfs(level, start):
    global path, min_cnt
    if level == 2:
        cnt = getsum(path)
        if cnt < min_cnt:
            min_cnt = cnt
        return
    for i in range(start+1, n):
        path[level] = i
        dfs(level+1, i)
        path[level] = 0


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    lst = [list(input()) for _ in range(n)]
    path = [0]*2
    min_cnt = 21e8
    dfs(0, 0)
    print(f'#{case} {min_cnt}')



'''
개선된 코드
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]
    ans = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            first = arr[0:i][:]
            two = arr[i:j][:]
            three = arr[j:N][:]

            cnt_first = [a.count('W') for a in first]
            cnt_two = [b.count('B') for b in two]
            cnt_three = [c.count('R') for c in three]

            result_first = len(first) * M - sum(cnt_first)
            result_two = len(two) * M - sum(cnt_two)
            result_three = len(three) * M - sum(cnt_three)

            ans.append(result_first + result_two + result_three)

    print(f'#{tc}', min(ans))
'''

'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW


1
4 5
WRWRW
BWRWB
WRWRW
RWBWR
'''
