def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        # 자기 자신은 우선 True.
        # 자기 자신이 아니면서 연결된 컴퓨터인데 방문하지 않았다면 DFS를 재귀적으로 다시 사용
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
                
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer