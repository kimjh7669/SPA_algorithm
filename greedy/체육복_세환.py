def solution(n, lost, reserve):
    reserve_1 = [r for r in reserve if r not in lost]
    lost_1 = [l for l in lost if l not in reserve]
    for num in reserve_1:
        if num + 1 in lost_1:
            lost_1.remove(num + 1)
        elif num - 1 in lost_1:
            lost_1.remove(num - 1)

    return n - len(lost_1)