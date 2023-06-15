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

    last = n-1 # u턴할 인덱스 = 방향이 바뀌는 인덱스

    def delivery(index):
        nonlocal bucket_deli
        cur_cap = cap
        for i in range(index, -1, -1):
            if bucket_deli[i]==0: continue
            elif cur_cap - bucket_deli[i]>=0:
                cur_cap -= bucket_deli[i]
                bucket_deli[i] = 0
            else:
                tmp = bucket_deli[i] - cur_cap
                cur_cap, bucket_deli[i] = 0, tmp
                break
        return

    def pickup(index):
        nonlocal bucket_pick
        cur_cap = cap
        for i in range(index, -1, -1):
            if bucket_pick[i]==0: continue
            elif cur_cap - bucket_pick[i]>=0:
                cur_cap -= bucket_pick[i]
                bucket_pick[i] = 0
            else:
                tmp = bucket_pick[i] - cur_cap
                cur_cap, bucket_pick[i] = 0, tmp
                break
        return

    distance = 0
    while last>=0:
        if bucket_deli[last]==0 and bucket_pick[last]==0:
            last -= 1
        else:
            delivery(last)
            pickup(last)
            distance += ((last+1)*2)

    return distance