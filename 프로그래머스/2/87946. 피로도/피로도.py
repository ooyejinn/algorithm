from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons):
        perm_k = k
        cnt = 0
        
        for i in perm:
            if perm_k >= i[0]:
                perm_k -= i[1]
                cnt += 1
                
        answer = max(cnt, answer)
    
    return answer