def solution(plans):
    answer = []
    def parse(time):
        hour, minute = time.split(':')
        return int(hour)*60 + int(minute)

    def reverse_parse(time):
        hour, minute = time//60, time % 60
        return str(hour) + ':' + str(minute)

    # 먼저 시작시간 순으로 정렬
    plans.sort(key=lambda x:x[1], reverse=True)

    stop = []
    cur = plans.pop()
    while plans:
        nxt = plans.pop()
        cur_start, cur_end = parse(cur[1]), parse(cur[1]) + int(cur[2])
        nxt_start = parse(nxt[1])

        if cur_end > nxt_start:
            dist = nxt_start - cur_start
            cur[2] = int(cur[2])-dist
            stop.append(cur[:])
            cur = nxt[:]
        elif cur_end == nxt_start:
            answer.append(cur[0])
            cur = nxt[:]
        else:# cur_end < nxt_start
            answer.append(cur[0])
            cur = nxt[:]
            if stop:
                stopped = stop.pop()
                stopped_start, stopped_end = cur_end, parse(stopped[1]) + int(stopped[2])
                stopped[1] = reverse_parse(stopped_start)
                if stopped_start < nxt_start:
                    cur = stopped[:]
                    plans.append(nxt[:])
                elif stopped_start >= nxt_start:
                    stop.append(stopped[:])
                    cur = nxt[:]
    if cur:
        answer.append(cur[0])
    while stop:
        stopped = stop.pop()
        answer.append(stopped[0])

    return answer