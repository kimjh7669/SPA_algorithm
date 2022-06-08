def solution(number, k):
    number = list(map(int,number))
    num = []
    num.append(number[0])
    for i in number[1:]:
        while len(num) != 0 and num[-1] < i and k > 0:
            k -= 1
            num.pop()
        num.append(i)
        
    if k > 0:
        for i in range(k):
            num.pop()
    answer = str(num[0])
    for i in num[1:]:
        answer += str(i)
    return answer
