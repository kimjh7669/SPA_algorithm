
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    distances = [0 for _ in range(n+1)]
    queue = []
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    queue.append(1)
    visited[1]=1
    while(len(queue) != 0):
        i = queue.pop(0)
        dis = distances[i]
        for node in graph[i]:
            if visited[node] == 0:
                visited[node]=1
                distances[node] = dis + 1
                queue.append(node)
    max_dis = max(distances)
    for dis in distances:
        if dis == max_dis:
            answer+=1
        
    return answer
