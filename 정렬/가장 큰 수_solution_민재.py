def solution(numbers):
    numbers = list(map(str, numbers))
    # 1. numbers를 reverse한 뒤 x에 넣음.
    # 2. 문자열 비교는 ASCII 값으로 치환되어 정렬됨. 각 문자열에 3을 곱해서 3자리수로 맞춘 뒤 첫 번째 인덱스 값으로 비교
    numbers.sort(key=lambda x: x * 3, reverse=True) 
    return str(int(''.join(numbers))) # '000'일때 int 씌워서 0으로 바꾼 뒤 다시 string으로 변환