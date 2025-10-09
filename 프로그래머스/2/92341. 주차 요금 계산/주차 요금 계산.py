import math
from collections import defaultdict

def solution(fees, records):
    #                          나누어 떨어지지 않으면 올림
    # fee: [기본 시간, 기본 요금, 추가 시간 단위, 추가 요금]
    # records: ["시각 차량번호 IN/OUT"]
    # answer: 차량번호 낮은 순으로, 주차 요금만 담아 정수 배열
    
    base_time, base_fee, add_time, add_fee = fees
    
    # 차량별 누적 주차 시간 (defaultdict: 키가 없을 경우 기본값 0)
    parking_time = defaultdict(int)
    
    # 차량별 입차 시각 (입차를 기록해두고, 후에 시간 계산할때 이걸 꺼내 쓰는게 나음)
    parking_in = {}
    
    for record in records:
        # 공백 기준으로 나누기
        time, car, action = record.split()
        
        # "HH:MM" 을 변환... 그냥 아예 분 단위로만 계산하는 게 나아서 그렇게 변환함
        hh, mm = map(int, time.split(":"))
        minutes = hh*60 + mm
        
        if action == "IN":
            parking_in[car] = minutes
        
        else:
            # 출차일 시 제거도 해야하니 pop으로 처리
            in_time = parking_in.pop(car)
            parking_time[car] += (minutes - in_time)
            
    # 23:59 출차 처리
    end_of_day = 23*60 + 59
    for car, in_time in parking_in.items():
        parking_time[car] += (end_of_day - in_time)
    
    answer = []
    
    # 차량 번호(key) 기준 오름차순 정렬
    for car in sorted(parking_time.keys()):
        total_minutes = parking_time[car]
        
        if total_minutes <= base_time:
            answer.append(base_fee)
            
        else:
            
            # 초과시간   math.ceil: 올림
            extra_fee = math.ceil((total_minutes - base_time) / add_time) * add_fee
            total_fee = base_fee + extra_fee
            answer.append(total_fee)
    
    return answer