def solution(brown, yellow):
    answer = []
    for b in range(1, int(yellow**0.5)+1):
        if yellow%b==0:
            a = yellow//b
            if (a+2)*(b+2)==brown+yellow:
                answer = [b+2, a+2] if b>a else [a+2, b+2]
                break
    return answer