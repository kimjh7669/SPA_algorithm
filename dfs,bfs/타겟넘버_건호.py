from collections import deque

def solution(numbers, target):
    answer = 0
    dfs = deque()
    dfs.append((numbers[0],0))
    dfs.append((-numbers[0],0))
    while dfs:
        num, idx = dfs.popleft()
        idx += 1
        if idx < len(numbers):
            dfs.append((num+numbers[idx],idx))
            dfs.append((num-numbers[idx],idx))
        else:
            if num == target:
                answer += 1
    return answer
