def solution(users, emoticons):
    amounts = [0]*len(users)
    max_amount = max_member = 0

    def dfs(emoticon_index):
        nonlocal amounts, max_amount, max_member
        if emoticon_index >= len(emoticons):
            members = total = 0
            for i in range(len(users)):
                if users[i][1] <= amounts[i]: members+=1
                else: total += amounts[i]
            if members > max_member or (members == max_member and total > max_amount):
                max_member = members
                max_amount = total
            return
        for discount in [10, 20, 30, 40]:
            tmp_amount = amounts[:]
            for i in range(len(users)):
                if users[i][0] <= discount:
                    amounts[i] += (emoticons[emoticon_index]*(100-discount)/100)
            dfs(emoticon_index+1)
            amounts = tmp_amount[:]
        return

    dfs(0)
    return [max_member, max_amount]