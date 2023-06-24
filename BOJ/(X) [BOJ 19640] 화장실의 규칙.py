N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
my_d, my_h = lst[K][0], lst[K][1]
count = 0
indexes = list(range(M))

# indexes는 스택과 같은 방식으로 작동
# indexes[i] 다음 인덱스 -> indexes[i+M]
# i==K%M인 경우(즉, 같은 줄에 서 있는 경우)
# i==K%M이고, indexes[i]==K인 경우 => 자신의 차례인 경우 => break
for _ in range(N//M+1):
  for i in range(M):
    print(indexes)
    index = indexes[i]
    d, h = lst[index]
    if d>my_d:
      count+=1
      indexes[i] += M
    elif d==my_d and h>my_h:
      count+=1
      indexes[i] += M
    elif d==my_d and h==my_h:
      if i<K%M:
        count+=1
        indexes[i] += M
      elif i==K%M and index != K:
        count+=1
        indexes[i] += M
      elif i==K%M and index == K:
        break
print(count)

'''
6 2 2
        1500 100-4
      1500 500-1
  1500 400-5
1500 400-2
  1500 200-6
1500 500-3



1 1
'''