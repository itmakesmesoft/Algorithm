# [SWEA] 1210. [S/W 문제해결 기본] 2일차 - Ladder1

난이도: D4</br>
문제 번호: 1210</br>
출처: [1210. \[S/W 문제해결 기본\] 2일차 - Ladder1](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh)</br>

</br>

**※ 무단 복제를 금하고 있으므로, 
    자세한 내용은 SW Expert 아카데미 문제 링크 참고**

</br>

### 풀이

```python
for _ in range(1,11):
    arr=[]
    idx = int(input())
    for j in range(100):
        arr.append(list(map(int, input().split())))

    x = arr[-1].index(2) # 도착지점의 x좌표
    y=98 # 현재의 y좌표 <= 도착지점보다 한칸 위부터 시작
    past = [] # 지나온 좌표를 넣을 리스트 생성
    while y > 0:
        # print(x, y)
        past.append((x, y)) 이전의 좌표를 리스트에 추가
        if x > 0:
            left = x-1
        else:
            left = x
        if x < 99:
            right = x+1
        else:
            right = x

        if arr[y][left]==1 and (left, y) not in past: # past에 없으면서 이동 가능한 경우(왼쪽)
            x=left
        elif arr[y][right]==1 and (right, y) not in past: # past에 없으면서 이동 가능한 경우(오른쪽)
            x=right
        else: # 위
            x = x
            y -= 1

    print(f'#{idx} {x}')
```