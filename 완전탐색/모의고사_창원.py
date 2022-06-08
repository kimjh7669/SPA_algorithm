def solution(answers):
    h_1 = [1,2,3,4,5]
    h_2 = [2,1,2,3,2,4,2,5]
    h_3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    a_ = 0
    b_ = 0
    c_ = 0
    for num in range(len(answers)):
        if answers[num] == h_1[num % 5]:
            a_ += 1
        if answers[num] == h_2[num % 8]:
            b_ += 1
        if answers[num] == h_3[num % 10]:
            c_ += 1

    list_ = [a_, b_, c_]
    max_ = max(list_)
    
    answer=[]
    for num in range(len(list_)):
        if list_[num] == max_:
            answer.append(num+1)
            
        
    return answer