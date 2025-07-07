def solution(progresses, speeds):
    # (100 - progress) // speed 만큼 걸림
    # 날짜도 카운트 해야됨
    # 그 뒤 그걸 어딘가에 담고 (며칠 뒤에 되는지 +i + 저 위의 day 만큼 더해서)
    
    n = len(speeds)
    successes = []
    
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        
        day = (100 - progress + speed - 1) // speed
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
    