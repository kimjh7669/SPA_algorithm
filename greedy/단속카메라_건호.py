def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    arr = []
    start = routes[0][1]
    arr.append(start)
    for i in range(1, len(routes)):
        if routes[i][0] <= start and routes[i][1] >= start:
            continue
        else:
            start = routes[i][1]
            arr.append(start)
    answer = len(arr)
    return answer
