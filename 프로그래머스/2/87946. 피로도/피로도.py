from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for cave in permutations(dungeons):
        now_k = k
        cnt = 0
        
        for required, cost in cave:
            if now_k >= required:
                now_k -= cost
                cnt += 1
            else:
                break
        
        answer = max(answer, cnt)
    
    return answer

# permutations([[a,b], [c,d], [e,f]])
# ([a,b], [c,d], [e,f])
# ([a,b], [e,f], [c,d])
# ([c,d], [a,b], [e,f])
# ([c,d], [e,f], [a,b])
# ([e,f], [a,b], [c,d])
# ([e,f], [c,d], [a,b])