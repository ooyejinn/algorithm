from collections import defaultdict

def solution(record):
    # 키: 유저 아이디
    # 밸류: 유저 닉네임
    # 다 해놓고 다시 record 뒤져서 행동 출력하기?
    
    answer = []
    nick_dict = defaultdict(str)
    
    for r in record:
        r = r.split()
        
        if r[0] == "Leave":
            continue
        
        nick_dict[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        
        if r[0] == "Enter":
            answer.append(nick_dict[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(nick_dict[r[1]] + "님이 나갔습니다.")
    
    return answer