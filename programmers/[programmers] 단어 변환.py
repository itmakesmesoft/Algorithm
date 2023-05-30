def solution(begin, target, words):

    def dfs(level, prev_word):
        nonlocal answer, begin, target, used
        if prev_word == target:
            answer = level
            return
        for i in range(len(words)):
            if used[i]==0:
                if check(words[i], prev_word):
                    used[i]=1
                    dfs(level+1, words[i])
                    used[i]=0

    def check(curr_word, prev_word):
        # curr_word의 알파벳이 prev_word과 일치하지 않는 알파벳 갯수를 반환
        count = 0
        for i, w in enumerate(curr_word):
            if w != prev_word[i]: count+=1
        return True if count == 1 else False # 1개이면 True, 초과 또는 미만이면 False

    answer = 0
    used = [0]*len(words)
    dfs(0, begin)
    return answer
