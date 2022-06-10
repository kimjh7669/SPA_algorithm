import copy

def dfs(tickets, depart, idx, route, visited):
    if idx == len(tickets)-1:
        return [route]
    routes = []
    tmp = []
    for i, ticket in enumerate(tickets):
        if i not in visited:
            if ticket[0] == depart:
                route_tmp = copy.deepcopy(route)
                visit_tmp = copy.deepcopy(visited)
                route_tmp.append(ticket[1])
                visit_tmp.append(i)
                routes = dfs(tickets, ticket[1], idx+1, route_tmp, visit_tmp)
                if len(routes) == 0:
                    continue
                for route1 in routes:
                    tmp.append(route1)
    if len(tmp) == 0:
        return []
    return tmp


def solution(tickets):
    answers = []
    depart = "ICN"
    for i, ticket in enumerate(tickets):
        if ticket[0] == depart:
            routes = dfs(tickets, ticket[1], 0, ["ICN", ticket[1]], [i])
            for route in routes:
                answers.append(route)
    tmp = answers[0]
    for answer in answers:
        for i in range(len(tmp)):
            if answer[i] < tmp[i]:
                tmp = answer
                break
            elif answer[i] > tmp[i]:
                break
    return tmp
