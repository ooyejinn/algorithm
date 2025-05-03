def solution(msg):
    chr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}
    for i in range(26):
        dict[chr[i]] = i + 1

    result = []
    nxt_idx = 27
    i = 0
    
    while i < len(msg):
        word = msg[i]
        
        # 만약 word가 dict에 있고,
        # 뒤에 글자를 더 붙일 수 있다면 계속하라
        while word in dict and i + len(word) <= len(msg):
            # (현재) 가장 길면서 사전에 있는 단어
            longest = word
            # 더 붙여도 msg 길이보다 안 넘는 상황이라면:
            if i + len(word) < len(msg):
                # 그 다음 글자를 word에 붙인다
                word += msg[i + len(word)]
            else:
                break
        
        # 가장 긴 단어의 번호를 결과에 추가
        result.append(dict[longest])
        
        # 새로운 단어 사전에 추가
        if i + len(longest) < len(msg):
            new_word = longest + msg[i + len(longest)]
            dict[new_word] = nxt_idx
            nxt_idx += 1
            
        # 현재 위치를 가장 긴 단어만큼 추가해 이동
        i += len(longest)

    return result