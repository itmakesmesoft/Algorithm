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

seconds = 0
def move():
  global seconds
  snake = deque()
  snake.append([1, 1]) # 길이는 오른쪽으로 증가
  direct = [[0,1],[1,0],[0,-1],[-1,0]]
  d = 0
  while True:
    y, x = snake[-1]
    if navigate: # 방향 전환하는지 판단
      s, dir = navigate.popleft()
      if int(s)==seconds:  # 방향 전환을 하는 경우, d 변경
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

    if ny>N or nx>N or ny<1 or nx<1: return # 벽에 부딪히는 경우
    else:
      for i in range(len(snake)):
        ty, tx = snake[i]
        if ny==ty and nx==tx: return # 자기 몸에 부딪히게 되는 경우

  # 사과 먹었는지 검증
    # 사과를 먹게되는 경우 => 꼬리 길어짐
    if f'{ny}_{nx}' in apples.keys() and apples[f'{ny}_{nx}']==1:
      apples[f'{ny}_{nx}']-=1
    else: # 사과를 안 먹게되는 경우 => 이동
      snake.popleft()
    snake.append([ny, nx])


move()
print(seconds)