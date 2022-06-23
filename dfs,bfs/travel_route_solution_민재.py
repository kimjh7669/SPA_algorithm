from collections import defaultdict
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    # defaultdict에 출발점과 도착점을 저장
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']})
    # 각 value를 내림차순으로 정리 (가능한 경로가 2개 이상일 때 알파벳 순서가 앞서는 경로를 선택하기 위함)
    for key in routes.keys():
        routes[key].sort(reverse=True)

    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
    # 출발과 도착 순서로 stack에 넣은 뒤 뒤에서부터 빼기
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer