def solution(number, k):
    a = [number[0]]
    for num in number[1:]:      
        while len(a) > 0 and a[-1] < num and k > 0:
            k -= 1
            a.pop()
        a.append(num)
    if k != 0:
        a = a[:-k]
    
    answer = "".join(a)
    return answer