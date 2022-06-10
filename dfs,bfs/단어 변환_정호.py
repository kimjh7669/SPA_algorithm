import copy

def dfs(cur_word, target, words, idx, visited, answer):
    if cur_word == target:
        return idx
    
    for i in range(len(cur_word)):
        temp1 = cur_word[0:i] + cur_word[i+1:]
        for j in range(len(words)):
            if j not in visited:
                temp2 = words[j][0:i] + words[j][i+1:]
                if temp1 == temp2:
                    temp = copy.deepcopy(visited)
                    temp.append(j)
                    num = dfs(words[j], target, words, idx+1, temp, answer)
                    if answer > num:
                        answer = num        
    return answer

def solution(begin, target, words):
    answer = 10000000
    for i in range(len(begin)):
        temp1 = begin[0:i] + begin[i+1:]
        for j in range(len(words)):
            temp2 = words[j][0:i] + words[j][i+1:]
            if temp1 == temp2:
                answer = dfs(words[j], target, words, 1, [j], answer)
    if answer == 10000000:
        answer = 0
    return answer
