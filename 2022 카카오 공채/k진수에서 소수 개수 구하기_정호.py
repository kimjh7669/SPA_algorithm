import math

def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def convert(n, k):
    num = ""
    while True:
        num_str = str(n%k)
        n = int(n//k)
        num = num_str + num
        if n == 0:
            break
    return num
    
def solution(n, k):
    answer = 0
    k_num = convert(n,k)
    num_list = k_num.split('0')
    
    for num in num_list:
        if num == '' or num == '1':
            continue
        answer += isprime(int(num))
    return answer
