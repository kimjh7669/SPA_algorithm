def solution(array, commands):
    answer = []
    for (i,j,k) in commands:
        current = array[i-1:j]
        current.sort()
        answer.append(current[k-1])
    return answer
