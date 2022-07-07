from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    mGap = -1e9
    items =  [0, 1,2,3,4,5,6,7,8,9,10]

    num_list = list(combinations_with_replacement(items, n))
    
    for candidate in num_list:
        info2 = [0] * 11
        ape, lio = 0, 0

        for score in candidate:
            info2[10 - score] += 1

        for score, (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                ape += (10 - score)
            else:
                lio += (10 - score)

        if lio > ape:
            gap = lio - ape
            if gap > mGap:
                mGap = gap
                answer = info2

    return answer
