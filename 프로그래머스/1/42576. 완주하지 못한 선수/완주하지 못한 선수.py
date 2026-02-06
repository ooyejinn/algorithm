def solution(participant, completion):
    d = {}
    
    for name in participant:
        d[name] = d.get(name, 0) + 1
    
    for name in completion:
        d[name] -= 1
    
    for name in d:
        if d[name] > 0:
            return name