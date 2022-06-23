from collections import deque

def solution(begin, target, words):
    answer = 0
    que = deque()
    que.append([begin, 0])
    V = [0 for i in range(len(words))]
    while que:
        word, cnt = que.popleft()
        # begin과 target이 같은 경우 0을 반환
        if word == target:
            answer = cnt
            break
        # 여기 정리!
        for i in range(len(words)):
            tmp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt +=1
                if tmp_cnt == 1:
                    que.append([words[i], cnt+1])
                    V[i] = 1
    return answer