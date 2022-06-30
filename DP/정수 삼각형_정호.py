def solution(triangle):
    visited = [[0 for j in range(501)] for i in range(501)]
    answer = 0
    
    for i in range(len(triangle)):
        for j in range(0, i+1):
            if i == 0:
                visited[i][j] = triangle[i][j]
            if i != 0 and j == 0:
                visited[i][j] = visited[i-1][j] + triangle[i][j]
            elif j == i:
                visited[i][j] = visited[i-1][j-1] + triangle[i][j]
            else:
                visited[i][j] = max(visited[i-1][j-1] + triangle[i][j], visited[i-1][j] + triangle[i][j])
    
                
    return max(visited[len(triangle)-1])
