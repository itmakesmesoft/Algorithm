def solution(r1, r2):
    total = 0

    def get_count(x):
        large_y = int((r2**2 - x**2)**(0.5))
        if x <= r1:
            y = (r1**2 - x**2)**(0.5)
            small_y = int(y) if y == int(y) else int(y)+1
        else:
            small_y = 0
        return large_y-small_y + 1

    for tmp_x in range(1, r2+1):
        total += get_count(tmp_x)

    total *= 4
    return total
