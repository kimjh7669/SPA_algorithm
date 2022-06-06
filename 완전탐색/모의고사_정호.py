def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct = [0,0,0]
    
    for i, ans in enumerate(answers):
        if ans == pattern1[i%5]:
            correct[0] += 1
        if ans == pattern2[i%8]:
            correct[1] += 1
        if ans == pattern3[i%10]:
            correct[2] += 1
    max_num = max(correct)
    
    for i in range(3):
        if max_num == correct[i]:
            answer.append(i+1)
            
    return answer
