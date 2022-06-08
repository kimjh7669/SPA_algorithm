def solution(brown, yellow):
    answer = []
    n = brown + yellow
    start = 3
    cnt = 2000001
    while start <= cnt:
        if n % start == 0:
            _cnt = n // start
            if  2*_cnt + 2 * start == brown + 4:
                cnt = _cnt
                _start = start
        start += 1
    answer = [_start,cnt]
    return answer
