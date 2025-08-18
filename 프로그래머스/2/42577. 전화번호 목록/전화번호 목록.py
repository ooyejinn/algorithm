def solution(phone_book):
    hash_map = {}
    
    for phone in phone_book:
        hash_map[phone] = 1
        
    for phone in phone_book:
        prefix = ""
        
        # 맨 마지막 원소 제외해서 보기
        # 자기자신을 체크해선 안 되고,
        # 같은 전번이 중복되지 않는다는 조건이 있기 때문
        # 역순은 [::-1]
        for num in phone[:-1]:
            prefix += num
            if prefix in hash_map:
                return False
            
    return True