def check_connection(connection, i, check):
    check.append(i)
    for j in connection[i]:
        if j not in check:
            check = check_connection(connection, j, check)
    return check

def solution(n, computers):
    answer = 0
    connection = {}
    for i in range(len(computers)):
        connection[i] = []
    for i in range(len(computers)):
        for j in range(i, len(computers[i])):
            if computers[i][j] == 1 and i != j:
                connection[i].append(j)
                connection[j].append(i)
    
    check = []
    for i in range(len(computers)):
        if i in check:
            continue
        contains = check_connection(connection, i, check)
        answer += 1
        
    
    return answer
