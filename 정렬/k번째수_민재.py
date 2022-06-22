def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        st_idx = i-1
        last_idx = j
        stlast_array = array[st_idx:last_idx]
        stlast_array.sort()
        answer.append(stlast_array[k-1])
    return answer