def solution(name):
    answer = 0
    to_list = []
    min_num = len(name) -1
    for idx, s in enumerate(name):
        if ord(s) - 65 < 13:    answer += ord(s) - 65
        else:   answer += 25 - (ord(s) - 66)    
        next_idx = idx+1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        min_num = min(min_num, 2*idx + len(name) - next_idx)
        min_num = min(min_num, idx + 2*(len(name)-next_idx))
        
    answer += min_num

    return answer
        
      
