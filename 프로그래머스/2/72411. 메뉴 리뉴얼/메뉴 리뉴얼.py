# 코스요리: 최소 2가지 이상의 단품메뉴 구성
# 최소 2명 이상의 손님에게 주문된 단품메뉴 조합만 메뉴 후보에 포함
# 아 이거 단품 하나만 볼 게 아니고 전체 조합을 봐야하네...? 황당한 문제네
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    # EX: orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    # EX: course = [2, 3, 4]
    
    # EX: c = 2 > 3 > 4 순으로 반복
    for c in course:
        combinations_list = []
        
        for order in orders:
            sorted_order = sorted(order)
            
                               # combinations(sorted_order, c)
                               # 정렬한 조합에서 c개짜리 조합 생성 
            combinations_list += combinations(sorted_order, c)
            
        # Couter 객체로 등장한 조합의 개수를 세기
        counter = Counter(combinations_list)
        
        if counter:
            # counter 객체의 횟수만 뽑음 (=가장 많이 등장한 "횟수")
            max_cnt = max(counter.values())
            
            if max_cnt >= 2:
                for combo, cnt in counter.items():
                    if cnt == max_cnt:
                        answer.append(''.join(combo))
    
    return sorted(answer)