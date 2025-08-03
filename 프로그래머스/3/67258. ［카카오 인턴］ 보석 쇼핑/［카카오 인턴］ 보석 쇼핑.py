from collections import defaultdict

def solution(gems):
    N = len(gems)
    M = len(set(gems))
    
    gem_dict = defaultdict(int)
    
    result_s = 0
    result_e = N-1
    
    start = 0
    
    # end 포인터를 하나씩 뒤로 민다 (추가 개념)
    for end in range(N):
        gem_dict[gems[end]] += 1
        
        while len(gem_dict) == M:
            if end - start < result_e - result_s:
                result_e = end
                result_s = start
                
            # 최소를 찾기 위해,
            # start 포인터를 하나씩 뒤로 민다 (제외 개념)
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
    
    return [result_s + 1, result_e + 1]