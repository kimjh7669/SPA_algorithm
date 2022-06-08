from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if people[0] + people[-1] > limit:
            answer += 1
            people.pop()
        else:
            x = people[0]
            people.pop()
            for i in range(len(people)):
                if  x + people[-1] <= limit:
                    x += people[-1]
                    people.popleft()
                else :
                    break
            answer += 1
                
    return answer
