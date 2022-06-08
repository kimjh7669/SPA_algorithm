def find(p, x):
    if p[x] != x:
        p[x] = find(p,p[x])
    return p[x]

def union(p, a, b):
    a = find(p,a)
    b = find(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    p = [0]
    for i in range(1,n+1):
        p.append(i)
    for i in costs:
        a, b, cost = i
        if find(p,a) != find(p,b):
            union(p,a,b)
            answer += cost
    

        
    return answer
