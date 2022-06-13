def solution(array, commands):
    answer = []
    
    for i, data in enumerate(commands):    
        min_i, max_j, k_th = data
        print(min_i, max_j, k_th)
        temp_arr = array[min_i-1:max_j]
        print(temp_arr)
        temp_arr.sort()
        print(temp_arr)
        answer.append(temp_arr[k_th-1])
        
    
    return answer