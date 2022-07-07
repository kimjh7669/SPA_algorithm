from copy import deepcopy

class tree_node():
    def __init__(self, node_type):
        self.parent = None
        self.child1 = None
        self.child2 = None
        self.node_type = node_type
        
    def set_parent(self, node):
        self.parent = node
    
    def set_child(self, node):
        if self.child1 == None:
            self.child1 = node
        else:
            self.child2 = node
    
def solution(info, edges):
    global answer
    answer = 0
    print(info)
    class_list = []
    visited = []
    for i in range(len(info)):
        visited.append(0)
        class_list.append(tree_node(info[i]))
    for i, j in edges:
        class_list[i].set_child(j)
        class_list[j].set_parent(i)
    def bfs(idx, goto_list, visited, sheep, wolf):
        global answer
        if class_list[idx].node_type == 0:
            sheep += 1
        else: 
            wolf += 1
            
        if sheep <= wolf:
            return
        if sheep > answer:
            answer = sheep
            
        child1 = class_list[idx].child1
        child2 = class_list[idx].child2
        if child1 != None:
            if visited[child1] == 0:
                goto_list.append(child1)
        if child2 != None:
            if visited[child2] == 0:
                goto_list.append(child2)
        for i in goto_list:
            goto_tmp = deepcopy(goto_list)
            goto_tmp.remove(i)
            visit_tmp = deepcopy(visited)
            visit_tmp[i] = 1
            bfs(i, goto_tmp, visit_tmp, sheep, wolf)
    bfs(0, [], visited, 0, 0)
        
        
    return answer
