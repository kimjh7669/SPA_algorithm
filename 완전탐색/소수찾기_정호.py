def comb(population,num):
	ans = []
	if num > len(population): return ans
	if num == 1:
		for i in population:
			ans.append([i])
	elif num>1:
		for i in range(len(population)-num+1): 
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True


def solution(numbers):
    answer = 0
    prime_list = []
    num_list = []
    for num in numbers:
        num_list.append(num)
    for i in range(len(numbers)):
        for com in comb(num_list,i+1):
            for per in permute(com):
                cur_num = int("".join(per))
                if is_prime(cur_num) and cur_num not in prime_list:
                    prime_list.append(cur_num)
                    answer += 1
                
    return answer
