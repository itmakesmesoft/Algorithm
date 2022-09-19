put = list(input())
n = int(input())

def getscore(put):
    score = 0
    for i in range(1, len(put)):
        a, b = put[i-1], put[i]
        if b>a:
            a, b = b, a
        if a==b:
            score -= 50
        elif ord(a)-ord(b)<=5:
            score += 3
        elif ord(a)-ord(b)>=20:
            score += 10
    return score

def dfs(level):
    global Max, put, memo
    if level == n:
        put = ''.join(put)
        if put in memo:
            score = memo[put]
        else:
            score = getscore(put)
            memo[put]=score
        if score > Max:
            Max = score
        return
    backup = put[:]

    for i in range(len(put)):
        for j in range(i, len(put)):
            put[i], put[j] = put[j], put[i]
            dfs(level+1)
            put = backup[:]

Max = -21e8
memo = {}
dfs(0)
print(Max)