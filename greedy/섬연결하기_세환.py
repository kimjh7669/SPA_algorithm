# 섬 연결하기
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    connect_id = [0] * n
    connect_id[costs[0][0]] = 1
    connect_id[costs[0][1]] = 1
    answer += costs[0][2]

    for i in range(1, n):
        if connect_id[costs[i][0]] + connect_id[costs[i][1]] == 2:
            continue
        else:
            connect_id[costs[i][0]] = 1
            connect_id[costs[i][1]] = 1
            answer += costs[i][2]
        if sum(connect_id) == n:
            break

    return answer