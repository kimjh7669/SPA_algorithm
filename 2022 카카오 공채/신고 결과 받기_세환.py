def solution(id_list, report, k):
    re_id = dict()
    answer = dict()
    
    for idx in id_list:
        re_id[idx] = set()
        answer[idx] = 0
    
    result_id = set()
    for idx in report:
        idl, re_idn = idx.split(" ")
        if idl not in re_id[re_idn]:
            re_id[re_idn].update([idl])
        
        if len(re_id[re_idn]) >= k:
            result_id.update([re_idn])
    
    if len(result_id) != 0:
        for res_id in result_id:
            for ans in re_id[res_id]:
                answer[ans] += 1
    
    
    return [*answer.values()]
