def solution(n, lost, reserve):
    
    # 학생에 기본 체육복 개수 1 부여
    students = {}
    for i in range(n):
        students[i+1] = 1
        
    # 잃어버린 경우 -1
    for n in lost:
        students[n] -= 1
        
    # 여분 있는 경우 +1
    for n in reserve:
        students[n] += 1
        
    # 앞 뒤로 여분이 있는 경우 빌려줌
    for key, value in students.items():
        if students[key] == 0:
            if key-1 in students:
                if students[key-1] == 2:
                    students[key] += 1
                    students[key-1] -= 1
                    continue
            if key+1 in students:
                if students[key+1] == 2:
                    students[key] += 1
                    students[key+1] -= 1
                    continue
        else:
            continue
    
    # 체육복이 1개 이상 있는 학생수 계산
    count = 0
    for key, value in students.items():
        if value > 0:
            count += 1
    return count