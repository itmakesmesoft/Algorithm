def solution(sizes):
    answer = 0
    max_n = max_m = 0
    for n, m in sizes:
        if n<m: n, m = m, n
        if n>max_n: max_n = n
        if m>max_m: max_m = m
    answer = max_n*max_m
    return answer