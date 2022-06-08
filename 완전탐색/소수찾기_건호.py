import math
import itertools
def primenumber(n):
    num = n
    arr = [False] * num
    arr[0] = True
    arr[1] = True
    
    for i in range(2,int(num ** 0.5)+1):
        if arr[i] == True  : continue
        for j in range(i+i, num,i):
            arr[j] = True
    return [i for i in range(2, num) if arr[i] == False]
def solution(numbers):
    answer = 0
    num_list = list(map(str,numbers))
    per = []
    for i in range(len(numbers)):
        i = i+1
        per += list(itertools.permutations(num_list,i))
    new = [int(("").join(p)) for p in per]
    new = list(set(new))
    pri_num = primenumber(max(new)+1)
    for i in new:
        if i in pri_num : answer += 1
    
    
    return answer
