def find(root_list, num):
    if num == root_list[num]:
        return num
    return find(root_list, root_list[num])

def union(root_list, num1, num2):
    num1_root = find(root_list, num1)
    num2_root = find(root_list, num2)
    if num1_root == num2_root:
        return root_list
    if num1_root < num2_root:
        root_list[num2] = num1_root
        for i in range(len(root_list)):
            if root_list[i] == num2_root:
                root_list[i] = num1_root
    else:
        root_list[num1] = num2_root
        for i in range(len(root_list)):
            if root_list[i] == num1_root:
                root_list[i] = num2_root
    return root_list

def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x : x[2])
    root_list = list(range(n))
    k = 1
    while k < n:
        for cost in costs:
            root1 = find(root_list, cost[0])
            root2 = find(root_list, cost[1])
            if root1 == root2:
                continue
            root_list = union(root_list, cost[0], cost[1])
            answer += cost[2]
            k += 1
            if k >= n:
                break
    
    
        
    return answer
