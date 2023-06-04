def solution(picks, minerals):
    answer = 0
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    min_total = int(21e8)
    
    def sum_array(pick, start, end, arr):
        cnt = 0
        tot = 0
        if len(arr) -1 < end:
            end = len(arr)
        for i in range(start, end):
            if minerals[i] == "diamond":
                tot += tired[pick][0]
            elif minerals[i] == "iron":
                tot += tired[pick][1]
            else:
                tot += tired[pick][2]
        return tot
            
            
    
    def dfs(index, total):
        nonlocal picks, min_total
        #1.남은 미네랄이 없는 경우
        if sum(picks)==0 or index >= len(minerals):
            if total < min_total:
                min_total = total
            return
            
        #2. 곡괭이 고르기.
        for i in range(3):
            if picks[i]>0:
                tmp = sum_array(i, index, index+5, minerals)
                picks[i] -= 1
                dfs(index+5,total+tmp)
                picks[i] += 1

  
    dfs(0,0)
    print(min_total)
    return min_total