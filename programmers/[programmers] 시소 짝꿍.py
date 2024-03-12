# 구글 참고

from collections import Counter

def solution(weights):
    counter = Counter(weights)
    count = 0

    for k, v in counter.items():
        if v>=2:
            count += v*(v-1)//2
        if k*2/3 in counter:
            count += counter[k*2/3]*v
        if k*2/4 in counter:
            count += counter[k*2/4]*v
        if k*3/4 in counter:
            count += counter[k*3/4]*v
    return count