n = int(input())
arr = list(map(int, input().split()))
result = []
stack = []
while True:
    if len(arr)==0 and len(stack)>=0: # arr에서 pop()할게 남아있지 않은 경우, 스택의 모든 원소를 result로 넣기
        result = result + stack
        break
    q = arr.pop(0) # arr에서 0번째 원소 pop
    if len(stack)==0: # 스택이 빈 경우 q를 stack에 삽입
        stack.append(q)
    else:
        p = stack.pop() 
        if p==q: # 스택에서 pop한 원소와 arr에서 pop한 원소가 같은 경우 stack에 삽입
            stack += [p, q]
        else: # 그렇지 않은 경우 result에 스택의 모든 요소 삽입(+p포함), q는 스택에 삽입
            result = result + stack +[p] 
            stack = [q]
        if len(stack)==3: # 똑같은 원소가 3개 나오는 경우 == len(stack)==3
            stack = []
            
# 삽입정렬
k = len(result)
for i in range(k):
    for j in range(i, 0, -1):
        if result[j] < result[j-1]:
            result[j], result[j-1] = result[j-1], result[j]
for i in range(k):
    print(result[i], end=' ')
    
'''
test case
17
5 4 5 1 1 1 1 1 2 2 2 3 3 3 3 8 1
'''