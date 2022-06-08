# 카펫
def solution(brown, yellow):
    al = brown + yellow
    n = al // 2 + 1

    a, b = 0,0
    for i in range(1, n+1):
        if al%i ==0:
            tmp = al//i
            if tmp > b and i >= tmp:
                a = i
                b = tmp
    answer = [a, b]
    return answer

