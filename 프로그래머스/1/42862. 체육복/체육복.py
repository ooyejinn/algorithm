def solution(n, lost, reserve):
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    sorted_lost = sorted(list(set_lost))
    
    for l in sorted_lost:
        if l - 1 in set_reserve:  # 앞 번호
            set_reserve.remove(l - 1)
        elif l + 1 in set_reserve:  # 뒷 번호
            set_reserve.remove(l + 1)
        else:
            n -= 1
            
    return n