def solution(numbers):
    answer = []
    stack = []
    for i in range(len(numbers)-1, -1, -1):
        while stack and numbers[i]>=stack[-1]:
            stack.pop()
        if stack==[]: answer.append(-1)
        else: answer.append(stack[-1])
        stack.append(numbers[i])
    answer.reverse()
    return answer