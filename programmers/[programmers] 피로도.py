def solution(k, dungeons): # k: 현재 피로도

    def dfs(cur_k, depth):
        nonlocal max_depth, used, l
        if depth > max_depth:
            max_depth = depth
        for i in range(l):
            if cur_k >= dungeons[i][0] and used[i] == 0:
                used[i] = 1
                dfs(cur_k-dungeons[i][1], depth+1)
                used[i] = 0

    max_depth = 0
    l = len(dungeons)
    used = [0]*l
    dfs(k, 0)
    return max_depth