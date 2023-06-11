from collections import deque

N = int(input())
K = int(input())

# 사과 위치 정보 얻기
apples = dict()
for _ in range(K):
  a, b = input().split()
  apples[a+'_'+b] = 1

# 방향 정보 얻기
L = int(input())
navigate = deque()
for _ in range(L):
  navigate.append(list(input().split()))


snake = deque()
snake.append([1, 1]) # 길이는 오른쪽으로 증가
seconds = 0
direct = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
while True:
  y, x = snake[-1]
  print("뱀 위치", y, x)
  # 방향 전환하는지 판단
  if navigate:
    s, dir = navigate.popleft()
    if int(s)==seconds:  # 방향 전환을 하는 경우, d 변경
      print(">>>> 방향 전환")
      if dir == 'D':
        d+=1
        if d>3: d=0
      elif dir == 'L':
        d-=1
        if d<0: d=3
    else: # 방향 전환을 하지 않는 경우
      navigate.appendleft([s, dir])

  # 다음에 이동할 좌표에 대한 검증
  ny, nx = y+direct[d][0], x+direct[d][1]
  seconds+=1

  # 사과 먹었는지 판단 (꼬리가 길어지는지 판단)
  # 사과를 먹게되는 경우
  if f'{ny}_{nx}' in apples.keys() and apples[f'{ny}_{nx}']==1:
    apples[f'{ny}_{nx}']-=1
    print("사과 먹음")
  else: # 사과를 안 먹게되는 경우
    snake.popleft()



  # 벽에 부딪히는 경우 -> break
  if ny>N or nx>N or ny<1 or nx<1:
    print('범위 벗어남', ny, nx)
    break
  else:
    print("다음 위치", ny, nx)
    print("뱀 좌표", *snake)
    for i in range(len(snake)):
      ty, tx = snake[i]
      # 자기 몸에 부딪히게 되는 경우 -> break
      if ny==ty and nx==tx:
        print('자기 몸에 부딪히는 경우', ny, nx, ty, tx)
        break
  snake.append([ny, nx])

print(seconds)