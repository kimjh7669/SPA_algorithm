def solution(n, lost, reserve):
    _lost = list(map(int,set(lost) - set(reserve)))
    _reserve = list(map(int,set(reserve) - set(lost)))
    for i in _reserve:
        back = i-1
        front = i+1
        if(back != 0) and (back in _lost):
            _lost.remove(back)
        elif(front != n+1) and (front in _lost):
            _lost.remove(front)
    return n - len(_lost)
