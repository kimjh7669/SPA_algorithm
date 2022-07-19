from itertools import combinations

def solution(orders, course):
    answer = []
    mapping = {}
    for i in range(26):
        mapping[i] = chr(i + 65)
    new_order = []
    for order in orders:
        new_order.append(sorted(order))
    orders = new_order
        
    for course_num in course:
        max_num = 0
        max_list = set()
        for order1 in orders:
            for com in combinations(order1, course_num):
                com_str = ''.join(com)
                num = 0
                for order2 in orders:
                    use = True
                    for com_chr in com_str:
                        if com_chr not in order2:
                            use = False
                            break
                    if use == True:
                        num += 1
                if num > 1 and max_num < num:
                    max_num = num
                    max_list = set()
                    max_list.add(com_str)
                elif num > 1 and max_num == num:
                    max_list.add(com_str)
        answer += max_list
                    
    return sorted(answer)
