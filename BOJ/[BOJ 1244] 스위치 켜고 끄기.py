'''
test case

8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''
n = int(input())
switches = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    gender, num = map(int, input().split())
    if gender == 1: # 남자 -> 배수인 경우 스위치 상태 변경(n번 스위치는 n-1번 인덱스)
        for i in range(n):
            if (i+1)%num==0:
                switches[i] = 1 - switches[i] # 상태변경

    else:           # 여자 -> num을 중심으로 양옆이 같은경우 상태 변경. 같지 않은 경우 num번 스위치만 상태 변경
        left = right = num-1 # num은 num-1번째 인덱스에 위치하므로, num-1을 기준점으로 함
        while left>=0 and right<n:
            if switches[left] == switches[right]:
                switches[left] = switches[right] = 1 - switches[left]
            else:
                break
            left -= 1
            right += 1
# 출력은 한줄에 최대 20개씩
for i in range(n):
    if i>0 and i%20 == 0:
        print()
    print(switches[i], end=' ')
        