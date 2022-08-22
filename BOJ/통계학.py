import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(int(sum(arr)/n+0.5)) # 산술평균
print(arr[n//2]) # 중앙값
print() # 최빈값
print(arr[-1]-arr[0]) #최댓값과 최솟값의 차이