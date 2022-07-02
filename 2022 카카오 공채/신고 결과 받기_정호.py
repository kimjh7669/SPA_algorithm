def solution(id_list, report, k):
    report = set(report)
    rev = {}
    id_num = {}
    answer = []
    
    for idx, i in enumerate(id_list):
        rev[i] = 0
        answer.append(0)
        id_num[i] = idx
        
    for i in report:
        j = i.split(' ')[1]
        rev[j]+=1
    
    dis = []
    for key, re in rev.items():
        if re >= k:
            dis.append(key)
    
    for i in report:
        m,n = i.split(' ')
        if n in dis:
            answer[id_num[m]]+=1
            
    return answer
