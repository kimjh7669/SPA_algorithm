def solution(numbers):
    answer=''
    _numbers = list(map(str,numbers))
    _numbers.sort(key=lambda x:x*3 ,reverse=True)
    answer = str(int(''.join(_numbers)))
    return answer
