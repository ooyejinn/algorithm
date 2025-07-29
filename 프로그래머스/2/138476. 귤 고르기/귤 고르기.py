from collections import defaultdict

def solution(k, tangerine):
    # 이거 허점 많은 쉬운 문제인듯 한데...?
    # 일단 defaultdict 하고
    # d.d에서 value가 k 이상 될때까지 key값을 +=1 하면 돼
    
    result = 0
    
    tangerine_type = defaultdict(int)
    
    for t in tangerine:
        tangerine_type[t] += 1
        
    # tangerine_type 딕셔너리를 value가 큰 순으로 정렬
    # 튜플의 리스트 [(크기1, 개수1), (크기2, 개수2), ...]
    sorted_tangerine_type = sorted(tangerine_type.items(), key=lambda x: x[1], reverse=True)
    
    cnt = 0
    
    for size, c in sorted_tangerine_type:
        cnt += c
        result += 1
        if cnt >= k:
            return result