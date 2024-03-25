def solution(data, col, row_begin, row_end):
    def int_to_binary(num):
        result = ""
        while num>0:
            result = str(num%2) + result
            num//=2
        return result
    data.sort(key=lambda x:(x[col-1], -1*x[0]))
    S = [0]*(len(data)+1)
    for i in range(row_begin, row_end+1):
        for num in data[i-1]:
            S[i] += num%i
    prev = ""
    for i in range(row_begin+1, row_end+1):
        if prev == "": prev = int_to_binary(S[i-1])
        B = int_to_binary(S[i])
        n = max(len(prev), len(B))
        prev = (n-len(prev))*"0"+prev
        B = (n-len(B))*"0"+B
        result = ""
        for j in range(n):
            if prev[j]!=B[j]: result += "1"
            else: result += "0"
        prev = result
    answer = 0
    for i in range(len(prev)):
        if prev[i]=="1":
            answer += 2**(len(prev)-i-1)
    return answer