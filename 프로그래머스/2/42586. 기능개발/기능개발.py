import math

def solution(progresses, speeds):
    
    n = len(speeds)
    successes = []
    
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        
        day = math.ceil((100 - progress) / speed)
        successes.append(day)
        
    answer = []
    fst = successes[0]
    cnt = 1
    
    for i in range(1, n):
        if successes[i] <= fst:
            cnt += 1
        else:
            answer.append(cnt)
            fst = successes[i]
            cnt = 1
    
    answer.append(cnt)
    return answer
    