# 4 구명 보트

def solution(people, limit):
    peo = sorted(people)
    answer = 0
    while len(peo) != 0:
        if len(peo) == 1:
            answer += 1
            break

        max_peo = peo.pop()
        min_peo = peo[0]
        if max_peo + min_peo > limit:
            answer += 1
        else:
            answer += 1
            peo.pop(0)

    return answer