def solution(new_id):
    # 1. 대문자 > 소문자 치환
    # 2. 알파벳, 숫자, -, _, . 제외한 모든 문자 제거
    # 3. .가 2번 이상 연속될 경우 1개로 줄임
    # 4. .가 맨 앞이나 맨 끝에 위치한다면 제거
    # 5. 빈 문자열이라면 a 대입
    # 6. 16자 이상일 경우 16자 이상부터 제거
    # 7. .가 맨 뒤에 위치할 경우 함께 제거
    # 8. 2자 이하라면, 마지막 문자를 길이가 3자 이상이 될 때까지 끝에 붙임
    
    answer_1 = new_id.lower()
    dictionary = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    answer_2 = ''
    
    for a in answer_1:
        if a in dictionary:
            answer_2 += a
    
    answer_3 = answer_2
    while '..' in answer_3:
        answer_3 = answer_3.replace('..', '.')
        
    answer_4 = answer_3.strip('.')
    
    if not answer_4:
        answer_5 = 'a'
    else:
        answer_5 = answer_4
        
    if len(answer_5) >= 16:
        answer_6 = answer_5[:15]
        answer_6 = answer_6.strip('.')
    else:
        answer_6 = answer_5
        
    answer_7 = answer_6
    while len(answer_7) <= 2:
        answer_7 += answer_7[-1]
    
    return answer_7