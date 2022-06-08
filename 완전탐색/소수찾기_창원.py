def solution(numbers):
    from itertools import permutations
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in p]
    
    for n in set(result):
        if descriptor(n):
            answer+=1
            
    return answer

def descriptor(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True