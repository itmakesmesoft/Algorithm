N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
me = lst[K][:]
count = 0
max_index = 0
for i in range(N):
  if i%M != K%M and i
  if lst[i][0]>me[0] or (lst[i][0]==me[0] and lst[i][1]>me[1]):
    count+=1

print(count)

'''
6 2 2
1500 100
1500 500
1500 400
1500 400
1500 200
1500 500
'''