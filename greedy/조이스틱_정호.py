def solution(name):
    answer = 0
    to_list = []

    for idx, char in enumerate(name):
        num = ord(char)
        if num == 65:
            continue        
        if num > 77:
            answer += (91-num)
            to_list.append(idx)
        else:
            answer += (num-65)
            to_list.append(idx)
    if len(to_list)== 0:
        min_num = 0    
    elif len(to_list) == 1:
        min_num = to_list[0]
        if min_num > len(name) - to_list[0]:
            min_num = len(name) - to_list[0]
    else:
        min_num = len(name)-to_list[0]
        
        for i in range(len(to_list)):
            if i == len(to_list)-1:
                if min_num > to_list[i]:
                    min_num = to_list[i]
            else:
                if min_num > (2*to_list[i]+(len(name) - to_list[i+1])):
                    min_num = (2*to_list[i]+(len(name) - to_list[i+1]))
                if min_num > (to_list[i]+2*(len(name) - to_list[i+1])):
                    min_num = (to_list[i]+2*(len(name) - to_list[i+1]))
            

    answer += min_num

    return answer
