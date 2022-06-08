def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    cnt_1, cnt_2, cnt_3 = 0,0,0
    s = 0
    for i in answers:
        if a[s%5] == i:
            cnt_1 +=1
        if b[s%8] == i:
            cnt_2 += 1
        if c[s%10] == i:
            cnt_3 += 1
        s += 1
    answer = [cnt_1, cnt_2, cnt_3]
    m = max(answer)
    index = [i+1 for i, v in enumerate(answer) if v == m ]
    return index
