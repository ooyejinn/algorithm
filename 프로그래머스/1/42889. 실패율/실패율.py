def solution(N, stages):
    #                                  1부터 N+1까지
    challengers = {i: 0 for i in range(1, N+2)}
    
    for stage in stages:
        challengers[stage] += 1
    
    fail_rates = {}
    
    now_players = len(stages)
    
    for i in range(1, N+1):
        if now_players == 0:
            fail_rates[i] = 0
        else:
            fail_rates[i] = challengers[i] / now_players
        
        now_players -= challengers[i]
        
    sorted_stages = sorted(fail_rates.items(), key=lambda x: (-x[1], x[0]))
    answer = [stage[0] for stage in sorted_stages]
        
    return answer