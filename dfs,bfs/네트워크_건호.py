from collections import deque
def solution(n, computers):
    check = [False] * (n)
    dfs = deque()
    ans = 0
    dist = [0] * (n)
    for i in range(n):
        if check[i] == False:
            ans += 1
            dfs.append((i,ans))
            check[i] = True
            while dfs:
                node, ans = dfs.popleft()
                for cur in range(n):
                    if cur == node:
                        pass
                    elif computers[node][cur] == 1 and check[cur] == False:
                        check[cur]=True
                        dist[cur] = ans
                        dfs.append((cur,ans))
    return ans
