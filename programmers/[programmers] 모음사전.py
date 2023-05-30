def solution(word):

    def dfs(level, prev_index, curr_word):
        nonlocal word, answer, flag, count, lst
        if curr_word == word:
            answer = count
            flag = True
            return
        if flag or level==5: return
        for i in range(5):
            count+=1
            dfs(level+1, i, curr_word+lst[i])

    lst = ['A', 'E', 'I', 'O', 'U']
    flag = False
    count = 0
    answer = 0
    dfs(0, 0, '')
    return answer