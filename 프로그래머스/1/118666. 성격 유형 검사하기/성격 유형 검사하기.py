def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    N = len(survey)
    
    for i in range(N):
        # RT
        q = survey[i]
        # 1~7
        c = choices[i]
        
        if c < 4:
            scores[q[0]] += 4 - c
        elif c > 4:
            scores[q[1]] += c - 4
    
    answer = ''
    
    if scores['R'] >= scores['T']:
        answer += 'R'
    else: answer += 'T'
    
    if scores['C'] >= scores['F']:
        answer += 'C'
    else: answer += 'F'
    
    if scores['J'] >= scores['M']:
        answer += 'J'
    else: answer += 'M'
    
    if scores['A'] >= scores['N']:
        answer += 'A'
    else: answer += 'N'
        
    return answer