'''
1     
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''

t = int(input())
for case in range(1, t+1):
    n, m, k = map(int, input().split()) # n 셀의 갯수, m 격리 시간, k 미생물 군집 수
    arr = [[[] for _ in range(n)] for _ in range(n)]
    print(arr)


    for i in range(k):
        y, x, num, d = map(int, input().split()) # y, x, 미생물수, 방향(1: 상, 2: 하, 3: 좌, 4: 우)
        arr[y][x].append([num, d])
        dy = [0,-1,1,0,0]
        dx = [0,0,0,-1,1]
        ny, nx = y+dy[d], x+dx[d]
        if ny>=n-1 or nx>=n-1 or ny<=0 or nx<=0: # 가장자리에 닿은 경우
            num//=2
            d = d-1 if d%2==0 else d+1
            arr[ny][nx].append([num, d])
    

'''
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''