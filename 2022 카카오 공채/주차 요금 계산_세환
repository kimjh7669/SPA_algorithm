import math
def minni(hm):
    hour = int(hm[:2])
    minu = int(hm[3:5])
    return hour*60 + minu

def solution(fees, records):
    car_num = dict()
    car_res = dict()
    car_tf = dict()
    for recor in records:
        n_reco = recor.split(" ")
        if n_reco[1] not in list(car_num.keys()):
            car_num[n_reco[1]] = 0
            car_res[n_reco[1]] = 0
            car_tf[n_reco[1]] = True
        
        if n_reco[2] == 'IN':
            car_num[n_reco[1]] += minni(n_reco[0])
            car_tf[n_reco[1]] = True
        else:
            car_res[n_reco[1]] += minni(n_reco[0]) - car_num[n_reco[1]]
            car_num[n_reco[1]] = 0
            car_tf[n_reco[1]] = False
    
    for key in car_tf.keys():
        if car_tf[key]:
            car_res[key] += minni("23:59") - car_num[key]
        
        if car_res[key] <= fees[0]:
            car_res[key] = fees[1]
        else:
            left_m = car_res[key] - fees[0]
            car_res[key] = fees[1] + math.ceil(left_m/fees[2])*fees[3]
    
    answer = [v for k, v in sorted(car_res.items(), key=lambda item: item[0])]
    
    return answer
