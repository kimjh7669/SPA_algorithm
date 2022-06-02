def solution(n, lost, reserve):
    found = []
    lost.sort()
    reserve.sort()
    for i in lost:
        if i in reserve:
            found.append(i)
            reserve.remove(i)
        elif i-1 in reserve:
            found.append(i)
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            if i+1 in lost:
                continue
            found.append(i)
            reserve.remove(i+1)
        
            
    return n - len(lost) + len(found)
