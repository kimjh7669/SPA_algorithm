def solution(name):
    default = 65
    default_ = 90
    alphabet = {} # 오른쪽으로 shift
    alphabet_ = {} # 왼쪽으로 shift
    for num in range(26):
        alphabet[num] = chr(default+num)
    
    alphabet = {v:k for k,v in alphabet.items()}

    for num in range(26):
        alphabet_[num+1] = chr(default_ - num)
    
    alphabet_ = {v:k for k,v in alphabet_.items()}

    shift_min = {} #
    shift_val = 0
    count = 0
    for a in name:  #각 알파벳 별 최소 변경수 지정
        if alphabet[a] < alphabet_[a]:
            shift_min[a] = alphabet[a]
            shift_val += alphabet[a]
        else:
            shift_min[a] = alphabet_[a]
            shift_val += alphabet_[a]
        
        if a == "A":
            count +=1

    # 알파벳 자리에 따른 고려
    shift_val += len(name)-1-count
    return shift_val