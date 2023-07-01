from copy import deepcopy
def solution(cap, n, deliveries, pickups):
    bucket_deli = deepcopy(deliveries)
    bucket_pick = deepcopy(pickups)

    # 배달, 수거, 경유
    # 배달은 가는 방향에만, 수거는 오는 방향에만 해야함
    # 갈때
        # 배달 또는 경유만 생각
    # 올때
        # 수거 또는 경유만 생각
    # 출발하면 다시 보관함으로 돌아와야 함
    # 맨 뒷집부터 배달, 맨 뒷집부터 수거
    # 점점 앞 인덱스의 집을 배달, 수거하는 방향으로 가야함

    deli_last = pick_last = n-1 # u턴할 인덱스 = 방향이 바뀌는 인덱스

    def delivery():
        nonlocal bucket_deli
        cur_cap = cap
        last = -1
        for i in range(deli_last, -1, -1):
            if bucket_deli[i]==0: continue
            else:
                if last<=i: last = i
                if cur_cap >= bucket_deli[i]:
                    cur_cap -= bucket_deli[i]
                    bucket_deli[i] = 0
                else:
                    tmp = bucket_deli[i] - cur_cap
                    cur_cap, bucket_deli[i] = 0, tmp
                    break
        return last

    def pickup():
        nonlocal bucket_pick
        cur_cap = cap
        last = -1
        for i in range(pick_last, -1, -1):
            if bucket_pick[i]==0: continue
            else:
                if last<=i: last = i
                if cur_cap >= bucket_pick[i]:
                    cur_cap -= bucket_pick[i]
                    bucket_pick[i] = 0
                else:
                    tmp = bucket_pick[i] - cur_cap
                    cur_cap, bucket_pick[i] = 0, tmp
                    break
        return last

    distance = 0
    while deli_last>=0 or pick_last>=0:
        if deli_last>=0: deli_last = delivery()
        if pick_last>=0: pick_last = pickup()
        distance += ((max(deli_last, pick_last)+1)*2)

    return distance