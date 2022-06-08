def solution(people, limit):
    people.sort()
    answer = 0
    heavy, light = len(people) - 1, 0 
    while heavy > light:
        if people[heavy] + people[light] <= limit: 
            heavy -= 1 
            light += 1
        else: 
            heavy -= 1 
        answer += 1
            
    if light == heavy: 
        answer += 1
    return answer