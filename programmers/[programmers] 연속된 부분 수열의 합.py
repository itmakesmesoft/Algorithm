def solution(sequence, k):
    
#  투 포인터로 접근
#  길이는 처음에는 늘어날 수 있음
#  부분 수열을 찾는 경우 -> 그 부분수열의 길이를 최대 길이로 설정
#  더 짧은 부분 수열을 찾는 경우에만 최대길이를 갱신
#  k를 만족하는 부분수열이 나오는 경우 -> 다음 투포인터는 start+1, end+1로 설정

    start = end = 0
    total = sequence[0]
    answer = []
    ln = len(sequence)
    max_len = ln
    
    while start < ln and end < ln:
        if total == k:
            if end-start < max_len:
                max_len = end-start
                answer = [start, end]
                
            if start+1 < ln:
                total -= sequence[start]
                start += 1
            if end+1 < ln:
                end += 1
                total += sequence[end]
            else: break
            
        elif total > k:
            total -= sequence[start]
            start += 1
        elif total < k:
            if end+1 < ln:
                end += 1
                total += sequence[end]
            else: break
    
    return answer