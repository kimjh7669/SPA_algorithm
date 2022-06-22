def solution(numbers, target):
    answer = 0
    leaves = [0]
    # leaves 리스트에 모든 가능한 덧셈 뺄셈의 경우를 담는다.
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    # target과 같은 경우만 answer에 추가
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer