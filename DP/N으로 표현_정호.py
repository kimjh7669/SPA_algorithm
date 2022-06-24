def check_num(num, times):
    global num_list
    if num>0 and num<32001: 
        if num_list[num]>times:
            num_list[num] = times
        
def check(num, N, idx):
    global num_list
    if idx > 8:
        return
    check_num(num, idx)
    check(num-N,N,idx+1)
    check(num+N,N,idx+1)
    check(num*N,N,idx+1)
    if num%N == 0:
        check(num//N,N,idx+1)

        
def solution(N, number):
    global num_list
    num_list = [10 for _ in range(32001)]
    answer = 0
    for i in range(5):
        tmp = int(str(N)*(i+1))
        if tmp < 32000:
            if num_list[tmp] > i+1:
                num_list[tmp] = i+1
                check(tmp,N,i+1)
            if num_list[tmp//N] > i+2:
                num_list[tmp//N] = i+2
                check(tmp//N,N,i+2)

    for i in range(2, 32001):
        time1= num_list[i]
        for j in range(1, 32001):
            time2 = num_list[j]
            tmp = i * j
            if tmp > 32001:
                break
            if time1 + time2 > 8:
                continue
            check(tmp,N, time1+time2) 
            tmp = i + j
            check(tmp,N, time1+time2)  
            tmp = i - j
            check(tmp,N, time1+time2) 
            
    if num_list[number] == 10:
        answer = -1
    else:
        answer = num_list[number]
    return answer
