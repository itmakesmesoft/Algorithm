def solution(numbers, target):
    answer = 0
    memo = []
    def dfs(level, tot, used):
        nonlocal answer, memo
        if level==len(numbers):
            if tot==target and used not in memo:
                memo.append(used)
                answer += 1
            return
        dfs(level+1, tot+numbers[level], used+'1')
        dfs(level+1, tot-numbers[level], used+'0')
    dfs(0, 0, '')
    return answer