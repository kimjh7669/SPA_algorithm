def solution(numbers):
    answer = ''
    
    new_numbers = []
    all_0 = True
    for num in numbers:
        if num != 0:
            all_0 = False
        new_numbers.append([int((str(num)*4)[:4]), str(num)])
    
    new_numbers = sorted(new_numbers, key = lambda x : x[0], reverse = True)
    for num in new_numbers:
        answer += num[1]
    if all_0 == True:
        answer = '0'
    return answer
