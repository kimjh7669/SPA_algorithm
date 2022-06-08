# 단속카메라
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    answer += 1
    cam = routes[0][1]

    for i in range(1, len(routes)):
        if cam < routes[i][0]:
            cam = routes[i][1]
            answer += 1

    return answer