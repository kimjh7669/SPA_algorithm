def solution(brown, yellow):
    answer = []
    garo = 0
    sero = 0
    for i in range(1, brown // 2):
        sero = i + 1
        garo = brown//2 - sero
        if (sero-1)*(garo-1) == yellow:
            return [garo+1, sero+1]
    return answer
