def solution(s):
    n = len(s)
    answer = n
    
    for unit_num in range(1, n//2+1):
        result = ""
        prev_str = s[0:unit_num]
        cnt = 1
        
        for i in range(unit_num, n, unit_num):
            now_str = s[i:i+unit_num]
            if prev_str == now_str:
                cnt += 1
            else:
                if cnt == 1:
                    result += prev_str
                else:
                    result += (str(cnt) + prev_str)
                prev_str = now_str
                cnt = 1

        if cnt == 1:
            result += prev_str
        else:
            result += (str(cnt) + prev_str)
        
        answer = min(answer, len(result))
                    
    return answer