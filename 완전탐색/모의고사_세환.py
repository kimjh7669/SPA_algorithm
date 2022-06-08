def solution(answers):
    n = len(answers)

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0] * 3
    for i in range(n):
        if one[i % 5] == answers[i]:
            cnt[0] += 1
        if two[i % 8] == answers[i]:
            cnt[1] += 1
        if three[i % 10] == answers[i]:
            cnt[2] += 1
    max_num = max(cnt)
    answer = []
    if max_num == cnt[0]:
        answer.append(1)
    if max_num == cnt[1]:
        answer.append(2)
    if max_num == cnt[2]:
        answer.append(3)

    return answer