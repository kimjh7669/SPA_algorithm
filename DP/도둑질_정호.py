def solution(money):
    answer = 0
    visited = [0 for i in range(len(money))]
    visited[0] = money[0]
    visited[1] = money[1]
    visited[2] = money[2] + visited[0]
    for i in range(2, len(money)-1):
        visited[i] = money[i] + max(visited[i-2], visited[i-3])
    answer = max(visited)
    
    visited = [0 for i in range(len(money))]
    visited[0] = 0
    visited[1] = money[1]
    visited[2] = money[2] + visited[0]
    for i in range(2, len(money)):
        visited[i] = money[i] + max(visited[i-2], visited[i-3])
        
    answer = max(answer, max(visited))
    return answer
