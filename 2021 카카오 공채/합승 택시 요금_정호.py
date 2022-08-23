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
    
    visited, s_dis_list = init_list(s, n)
    s_dis_list = dijkstra(visited, s_dis_list, s, n)
    
    answer = inf
    for i in range(1,n+1):
        mid_dis = s_dis_list[i]
        mid_visited, mid_dis_list = init_list(i, n)
        mid_dis_list = dijkstra(mid_visited, mid_dis_list, i, n)
        if answer > (mid_dis + mid_dis_list[a] + mid_dis_list[b]):
            answer = (mid_dis + mid_dis_list[a] + mid_dis_list[b])
    
    return answer
