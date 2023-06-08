def solution(enroll, referral, seller, amount):
    # seller 순회하며 amount *100 계산 후 10%를 추천인에게 보내기 => 재귀형태
    def cal_profit(name, profit):
        nonlocal indexes, profits
        fee = int(profit*0.1) # 추천인이 가져야 할 돈
        refer = referral[indexes[name]] # 추천인 이름
        if refer == '-':
            profits[indexes[name]] += profit-fee # 수익은 profits에 기록(인덱스 순)
            return
        elif fee < 1: # 1원 미만인 경우 추천인에게 보내지않음
            profits[indexes[name]] += profit
            return
        else:
            pass
            profits[indexes[name]] += profit-fee
            cal_profit(refer, fee)


    indexes = {} # name의 인덱스 값(enroll의 인덱스)이 담기는 딕셔너리
    for index, name in enumerate(enroll):
        indexes[name]=index

    profits = [0]*len(enroll)

    for i, ea in enumerate(amount):
        name = seller[i] # 판매원 이름
        profit = 100*ea # 이익
        cal_profit(name, profit)

    return profits