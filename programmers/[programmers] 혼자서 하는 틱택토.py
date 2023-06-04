def solution(board):  
    # O 개수는 반드시 X와 같거나 +1 많아야 함 또는 선공이 X인 경우
    # O가 3개 연속(가로 세로 대각선)인데 X도 3개 연속인 경우
    # O가 3개 연속(가로 세로 대각선)인데 X가 O와 같은 갯수인 경우
    def counter():
        nonlocal count
        for i in range(3):
            for j in range(3):
                if board[i][j]=='O':
                    count[0]+=1
                elif board[i][j]=='X':
                    count[1]+=1
        return count

    # 가로 세로 대각선 체커
    def checker():
        nonlocal status_o, status_x
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                if board[i][0]=='O':
                    status_o = True
                elif board[i][0]=='X':
                    status_x = True
            elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i]=='O':
                    status_o = True
                elif board[0][i]=='X':
                    status_x = True
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[1][1]=='O':
                status_o = True
            elif board[1][1]=='X':
                status_x = True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[1][1]=='O':
                status_o = True
            elif board[1][1]=='X':
                status_x = True
                
    status_o = status_x = False
    count = [0, 0] # [O갯수, X갯수]
    
    checker()
    counter()
    if (status_o and status_x) or (status_o and count[0] == count[1]) or (status_x and count[0] > count[1]):
        answer = 0
    elif count[0] < count[1] or count[0] -1 > count[1]:
        answer = 0
    else:
        answer = 1
    
    return answer