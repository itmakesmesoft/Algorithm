t = int(input())
for case in range(1, t+1):
    stack = list(input())
    res = []
    while stack:
        s = stack.pop()
        res.append(s)
        if len(res)>1:
            for i in range(1, len(res)):
                if res[i]==res[i-1]:
                    del res[i-1:i+1]
    print(f'#{case} {len(res)}')