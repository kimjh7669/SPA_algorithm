from copy import deepcopy
def solution(n, info):
    answer = []
    score = [10 - i for i in range(11)]
    def dfs(idx, r_list, r_score, a_score, remain_num):
        if idx == 10:
            # 마지막엔 남은 숫자 무조건 써야한단다.
            r_list.append(remain_num)
            answer.append([r_score - a_score, r_list])
            return
        elif remain_num == 0:
            r_list.append(remain_num)
            if info[idx] != 0:
                a_score += score[idx]
            dfs(idx+1, r_list, r_score, a_score, remain_num)
        else:
            # 쏨
            r_list_tmp = deepcopy(r_list)
            remain_num_tmp = remain_num
            if info[idx] != 0:  # 어피치가 쏜거임
                if remain_num_tmp - info[idx] - 1 >= 0:
                    r_list_tmp.append(info[idx] + 1)
                    remain_num_tmp -= info[idx] + 1
                    dfs(idx+1, r_list_tmp, r_score + score[idx], a_score, remain_num_tmp)    
            else:               # 어피치가 안쏜거임
                r_list_tmp.append(1)
                remain_num_tmp -= 1
                dfs(idx+1, r_list_tmp, r_score + score[idx], a_score, remain_num_tmp)    
            # 안쏨
            r_list_tmp = deepcopy(r_list)
            r_list_tmp.append(0)
            if info[idx] != 0:
                dfs(idx+1, r_list_tmp, r_score, a_score+score[idx], remain_num)
            else:
                dfs(idx+1, r_list_tmp, r_score, a_score, remain_num)
    dfs(0, [], 0, 0, n)
    answer.sort(key=lambda x:x[0], reverse = True)
    if answer[0][0] <= 0:
        return [-1]
    max_dis = answer[0][0]
    real_answer = answer[0][1]
    for i in range(len(answer)):
        if answer[i][0] < max_dis:
            break
        for j in range(10, -1, -1):
            if real_answer[j] == answer[i][1][j]:
                continue
            elif real_answer[j] < answer[i][1][j]:
                real_answer = answer[i][1]
            else:
                break
    return real_answer
