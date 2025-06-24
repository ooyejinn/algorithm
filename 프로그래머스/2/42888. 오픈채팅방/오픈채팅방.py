def solution(record):
    answer = []
    user_nick = {}
    
    for r in record:
        parts = r.split()
        active = parts[0]
        uid = parts[1]
        
        if active == "Enter" or active == "Change":
            user_nick[uid] = parts[2]
    
    for r in record:
        parts = r.split()
        active = parts[0]
        uid = parts[1]
        if active == "Enter":
            answer.append(f"{user_nick[uid]}님이 들어왔습니다.")
        elif active == "Leave":
            answer.append(f"{user_nick[uid]}님이 나갔습니다.")
    
    return answer