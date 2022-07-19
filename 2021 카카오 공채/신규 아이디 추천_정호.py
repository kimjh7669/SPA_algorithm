def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    check = "-_."
    for i in new_id:
        j = ord(i)
        if j >= 48 and j <= 57:
            answer += i
            continue
        elif j >= 97 and j <= 122:
            answer += i
            continue
        elif i in check:
            answer+= i
            continue
    
    # 3단계
    check_dot = False
    new_id = answer
    answer = ''
    for idx, i in enumerate(new_id):
        if i == '.':
            if check_dot == True:
                continue
            else:
                check_dot = True
                answer += i
        else:
            check_dot = False
            answer += i
    
    # 4단계
    if len(answer) != 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) != 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer
