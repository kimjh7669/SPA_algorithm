signs = [-1, 1]

def check(numbers, cur_num, target, idx, answer):
    if idx >= len(numbers):
        if cur_num == target:
            return answer + 1
        else:
            return answer
    
    for sign in signs:
        next_num = cur_num+ sign * numbers[idx]
        answer = check(numbers, next_num, target, idx+1, answer)
    return answer
    
def solution(numbers, target):
    answer = 0
    answer = check(numbers, 0, target, 0, answer)
    return answer
