mapping = {}
mapping['-'] = 0
mapping['cpp'] = 27 
mapping['java'] = 54
mapping['python'] = 81
mapping['backend'] = 9
mapping['frontend'] = 18
mapping['junior'] = 3
mapping['senior'] = 6
mapping['chicken'] = 1
mapping['pizza'] = 2

from itertools import combinations

def solution(info, query):
    answer = []
    infos = []
    info_tree = [[] for _ in range(4*3*3*3)]
    
    for i in info:
        infos.append(i.split(' '))
    
    # tree로 만들어서 각 점수를 index에 맞춰서 append
    for info in infos:
        map_num = 0
        for i, inf in enumerate(info):
            try:
                map_num += mapping[inf]
            except:
                score = int(inf)
        info_tree[0].append(score)
        info_tree[map_num].append(score)
        for i in range(3):
            for combi in combinations(range(4), i+1):
                map_num = 0
                for com in combi:
                    map_num += mapping[info[com]]
                info_tree[map_num].append(score)
        
    for i in range(108):
        info_tree[i] = sorted(info_tree[i])
    
    
    # query string 전처리
    querys = []    
    for i in query:
        temp = []
        for j in i.split(' '):
            if j != "and":
                temp.append(j)
        querys.append(temp)
    
    # query 별로
    for query in querys:
        ans = 0
        map_num = 0
        for i in range(5):
            if i == 4:
                score = int(query[i])
                break
            map_num += mapping[query[i]]
            
        temp = info_tree[map_num]
        left = 0 
        right = len(temp)-1
        
        while left<= right:
            if left == right:
                if left == 0:
                    if temp[left] >= score:
                        ans = left + 1
                        break
                else:
                    if temp[left-1] >=score:
                        left -= 1
                
            mid = (left+right)//2
            if temp[mid] == score:
                if mid == 0:
                    ans = 1
                    break
                else:
                    if temp[mid-1] >= score:
                        right -= 1
                        if left != 0:
                            left -=1
                    else:
                        ans = mid + 1
                        break
            elif temp[mid] < score:
                if mid >= len(temp) - 1:
                    break
                elif temp[mid+1] >= score:
                    ans = mid + 2
                    break
                else:
                    left = mid + 1
            elif temp[mid] > score:
                if mid == 0:
                    ans = 1
                    break
                elif temp[mid-1]<score:
                    ans = mid+1
                    break
                elif temp[mid-1]<=score:
                    right -= 1
                    if left != 0:
                        left -=1
                else:
                    right = mid - 1 
        
        if ans != 0:
            ans = len(temp) - ans+1
        
        answer.append(ans)
            
    return answer
