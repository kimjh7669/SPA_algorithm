def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

numbers = [4,1,2,1]
target = 3
a = solution(numbers, target)