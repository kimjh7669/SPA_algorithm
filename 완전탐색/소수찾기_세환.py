# 소수찾기
def solution(numbers):
    all_case = []

    def recur(tmp, a, all_case):

        if len(a) == 0:
            return all_case

        for i in range(len(a)):
            sta = a[i]
            n_tmp = tmp + sta
            all_case.append(int(n_tmp))
            if i == 0:
                b = a[1:]
            elif i == len(a) - 1:
                b = a[:-1]
            else:
                b = a[:i] + a[i + 1:]
            recur(n_tmp, b, all_case)

        return all_case

    all_case = recur('', numbers, all_case)
    all_case = set(all_case)

    cnt = 0
    for num in all_case:
        if num < 2:
            continue
        if num == 2:
            cnt += 1
            continue

        for per in range(2, num):
            if num % per == 0:
                break
        else:
            cnt += 1
    return cnt