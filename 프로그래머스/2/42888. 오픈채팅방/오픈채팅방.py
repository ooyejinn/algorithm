def solution(record):
    result = []
    user_nick = {}
    
    for r in record:
        parts = r.split()
        cmd = parts[0]
        uid = parts[1]
        
        if cmd == "Enter" or cmd == "Change":
            nick = parts[2]
            user_nick[uid] = nick
    
    for r in record:
        parts = r.split()
        cmd = parts[0]
        uid = parts[1]
        
        if cmd == "Enter":
            result.append(f"{user_nick[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            result.append(f"{user_nick[uid]}님이 나갔습니다.")
    
    return result