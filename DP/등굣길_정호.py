visited = [[0 for _ in range(101)] for i in range(101)]
def solution(m, n, puddles):
    answer = 0
    visited[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                visited[i][j] = visited[0][j-1]
            elif j == 0:
                visited[i][j] = visited[i-1][0]
            else:
                visited[i][j] = visited[i-1][j] + visited[i][j-1]
            if [i+1,j+1] in puddles:
                visited[i][j] = 0
    
    return visited[m-1][n-1]%1000000007
