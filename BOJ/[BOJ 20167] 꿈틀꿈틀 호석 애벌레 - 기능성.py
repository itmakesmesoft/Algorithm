N, K = map(int, input().split())
lst = list(map(int, input().split()))

def recur(index, status, satisfaction, energy):
    global max_energy
    if satisfaction >= K:
        energy += (satisfaction-K)
        status = False
    if index == N:
        if energy > max_energy:
            max_energy = energy
        return

    if status:
        recur(index+1, True, satisfaction+lst[index], energy)
    else:
        recur(index+1, True, lst[index], energy)
        recur(index+1, False, 0, energy)


max_energy = 0
recur(0,False,0,0)
print(max_energy)