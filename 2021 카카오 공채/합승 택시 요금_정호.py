inf = 1000000000
fare_graph = [[] for _ in range(201)]

def init_list(start, n):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    dis_list = [inf for _ in range(n+1)]
    dis_list[start] = 0
    return visited, dis_list

def get_smallest_node(dis_list, visited, n):
    min_dis = inf
    min_idx = 0
    for i in range(1, n+1):
        if visited[i] == 0 and min_dis > dis_list[i]:
            min_dis = dis_list[i]
            min_idx = i
    return min_idx
    
    
def dijkstra(visited, dis_list, start, n):
    global fare_graph
    for node, dis in fare_graph[start]:
        dis_list[node] = dis
    
    for _ in range(n-1):
        s_node = get_smallest_node(dis_list, visited, n)
        visited[s_node] = 1
        for node, dis in fare_graph[s_node]:
            if dis_list[node] > dis_list[s_node] + dis:
                dis_list[node] = dis_list[s_node] + dis
    return dis_list

def solution(n, s, a, b, fares):
    for c,d,f in fares:
        fare_graph[c].append([d,f])
        fare_graph[d].append([c,f])
    
    visit, s_list = init_list(s, n)
    s_list = dijkstra(visit, s_list, s, n)
    visit, a_list = init_list(a, n)
    a_list = dijkstra(visit, a_list, a, n)
    visit, b_list = init_list(b, n)
    b_list = dijkstra(visit, b_list, b, n)
    
    answer = inf
    for i in range(1,n+1):
        if answer > s_list[i] + a_list[i] + b_list[i]:
            answer = s_list[i] + a_list[i] + b_list[i]
    
    return answer
