def solution(s):
    n = len(s)
    answer = n
    
    for unit_num in range(1, n // 2 + 1):
        result = ""
        prev_str = s[0:unit_num]
        cnt = 1
        
        # 0부터 n까지 cut_num 씩 증가
        for i in range(unit_num, n, unit_num):
            # 직전것과 똑같이 반복될 경우
            if s[i:i+unit_num] == prev_str:
                cnt += 1
            
            else:
                result += str(cnt) + prev_str if cnt > 1 else prev_str
                prev_str = s[i:i+unit_num]
                cnt = 1
                
        result += str(cnt) + prev_str if cnt > 1 else prev_str
        
        answer = min(answer, len(result))
    
    return answer