def solution(targets):
#     targets 정렬
    targets.sort(key=lambda x:x[0],  reverse=True)
#     [[11,13],[10,14],[5,12],[4,8],[4,5],[3,7],[1,4]]	
    
#     겹치는 구간이 있는지 체크하고, 겹치는 구간으로 범위를 축소
    t_start, t_end = targets.pop()
    range_start, range_end = t_start, t_end
    cnt = 1
    while targets:
        t_start, t_end = targets.pop()
        if t_start <= range_start and t_end>=range_end: continue
        else:
            range_start = t_start
            if t_start>=range_end:
                range_end = t_end
                cnt+=1
            elif t_start>=range_start and t_start<range_end and t_end<=range_end:
                range_end = t_end
    return cnt