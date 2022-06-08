# ex3)큰 수 만들기

def solution(number, k):
    answer = []
    c = 0
    for max_num in range(9, -1, -1):
        for j, num in enumerate(number):
            if num == str(max_num):
                if j <= len(number) - k - 1:
                    c += 1
                    break
        if c == 1:
            break

    answer.append(num)
    k -= j

    for i in number[j + 1:]:
        while answer and answer[-1] < i and k > 0:
            k -= 1
            answer.pop()
        answer.append(i)
    return "".join(answer[:len(answer) - k])