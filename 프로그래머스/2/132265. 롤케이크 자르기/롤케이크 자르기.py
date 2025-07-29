from collections import defaultdict

def solution(topping):
    cnt = 0
    
    left_set = set()
    right_cnt = defaultdict(int)
    
    for t in topping:
        right_cnt[t] += 1
        
    for t in topping:
        left_set.add(t)
        right_cnt[t] -= 1
        
        if right_cnt[t] == 0:
            del right_cnt[t]
            
        if len(left_set) == len(right_cnt):
            cnt += 1

    return cnt