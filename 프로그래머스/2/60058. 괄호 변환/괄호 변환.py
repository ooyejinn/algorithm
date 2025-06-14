# 올바른 괄호 문자열인지 판단
def is_correct(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    # 스택이 비어있으면 올바른 괄호 문자열
    return not stack


# u, v 분리
def split_phrase(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
            
        # 수 맞는 순간 (균형잡힌) 바로 return
        if left == right:
            return p[:i+1], p[i+1:]

        
def reverse_p(s):
    result = ""
    for char in s:
        if char == "(":
            result += ")"
        else:
            result +="("
    return result
    
        
def solution(p):
    if not p:
        return ""
    
    u, v = split_phrase(p)
    
    if is_correct(u):
        # u가 올바른 문자열일 경우, v를 재귀 처리하고 뒤에 붙인다
        return u + solution(v)
    else:
        # u가 올바르지 않을 경우 4번 수행
        return "(" + solution(v) + ")" + reverse_p(u[1:-1])