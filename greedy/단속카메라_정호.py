def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x : x[1])
    cur_time = -40000
    for route in routes:
        if cur_time < route[0]:
            cur_time = route[1]
            answer += 1
    return answer
