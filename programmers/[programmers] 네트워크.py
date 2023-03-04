def solution(n, computers):
    def dfs(num):
        for i in range(n):
            if visited[i]==1: continue
            if computers[num][i]==1:
                visited[i]=1
                dfs(i)

    answer = 0
    visited= [0]*n
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            dfs(i)
            answer+=1
    return answer