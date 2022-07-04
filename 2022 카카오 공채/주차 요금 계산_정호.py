import math

def solution(fees, records):
    answer = []
    cars = set()
    for record in records:
        cars.add(int(record.split(' ')[1]))
    cars = sorted(cars)
    car_dict={}
    for car in cars:
        car_dict[car] = []
        
    for record in records:
        time, car, in_out = record.split(' ')
        time1, time2 = time.split(":")
        time = int(time1)*60 + int(time2)
        car_dict[int(car)].append(time)
    
    car_dict2 = {}
    for key, value in car_dict.items():
        if len(value)%2==1:
            value.append(23*60 + 59)
        num = - sum(value[::2]) + sum(value[1::2])
        answer.append(fees[1] + fees[3]*(math.ceil(max(0,num-fees[0])/fees[2])))
            
    return answer
