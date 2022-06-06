def solution(people, limit):
    people.sort()
    
    answer1 = 0
    last_index = len(people) - 1
    for i in range(len(people)):
        while i < last_index:
            if people[i] + people[last_index] <= limit:
                answer1 += 1  
                last_index -= 1
                break
            last_index -= 1
            
    return len(people) - answer1
